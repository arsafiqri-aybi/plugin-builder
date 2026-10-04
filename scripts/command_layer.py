#!/usr/bin/env python3
"""Parse concise Plugin Builder command aliases without eval and emit a canonical plan."""
import argparse
import ast
import json
import re
from urllib.parse import urlparse

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CREATE_ALIASES = {"create_personal_plugin", "create_private_plugin_from_mcp"}
ALLOWED_CREATE_KEYS = {"mcp_url", "name", "display_name", "description", "author"}

def normalize_name(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.strip().lower())
    return re.sub(r"-+", "-", value).strip("-")[:64]

def infer_name(url: str) -> str:
    host = (urlparse(url).hostname or "").lower()
    labels = [x for x in host.split(".") if x]
    if not labels:
        raise ValueError("cannot infer plugin name from MCP URL")
    candidate = labels[0]
    if candidate in {"mcp", "api", "www"} and len(labels) > 1:
        candidate = labels[1]
    name = normalize_name(candidate)
    if not name or not NAME_RE.fullmatch(name):
        raise ValueError("inferred plugin name is invalid; provide name explicitly")
    return name

def validate_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError("remote MCP URL must be an absolute https:// URL")
    if parsed.username or parsed.password:
        raise ValueError("MCP URL must not contain embedded credentials")
    return url

def literal(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (str, int, float, bool, type(None))):
        return node.value
    raise ValueError("command arguments must be literal values")

def parse_command(text: str) -> dict:
    expr = ast.parse(text.strip(), mode="eval").body
    if not isinstance(expr, ast.Call) or not isinstance(expr.func, ast.Name):
        raise ValueError("expected a creator-style command call")
    command = expr.func.id
    if command not in CREATE_ALIASES:
        raise ValueError(f"unsupported command alias: {command}")
    if expr.args:
        raise ValueError("use keyword arguments only")
    args = {}
    for kw in expr.keywords:
        if kw.arg is None or kw.arg not in ALLOWED_CREATE_KEYS:
            raise ValueError(f"unsupported argument: {kw.arg}")
        if kw.arg in args:
            raise ValueError(f"duplicate argument: {kw.arg}")
        args[kw.arg] = literal(kw.value)
    if "mcp_url" not in args or not isinstance(args["mcp_url"], str):
        raise ValueError("mcp_url is required")
    url = validate_url(args["mcp_url"].strip())
    name = normalize_name(str(args.get("name") or infer_name(url)))
    if not NAME_RE.fullmatch(name):
        raise ValueError("invalid plugin name")
    display = str(args.get("display_name") or name.replace("-", " ").title()).strip()
    description = str(args.get("description") or f"Connect ChatGPT to the {display} MCP server.").strip()
    author = args.get("author")
    return {
        "command": command,
        "intent": "create_private_plugin_from_existing_remote_mcp",
        "source": {"kind": "remote_mcp", "url": url, "transport": "streamable-http"},
        "plugin": {
            "name": name,
            "display_name": display,
            "description": description,
            "author": author,
        },
        "workflow": [
            "probe_mcp_when_supported",
            "generate_minimal_package",
            "validate_and_audit",
            "check_duplicate_or_existing_source",
            "discover_host_create_adapter",
            "create_from_archive_if_available",
            "read_back_persisted_state",
            "verify_connection_auth_and_smoke_when_supported",
        ],
        "required_host_privilege": "authenticated private-plugin create action",
        "fallback_state": "PACKAGE_READY",
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("command")
    a = p.parse_args()
    try:
        plan = parse_command(a.command)
    except (SyntaxError, ValueError) as exc:
        print(f"command parse failed: {exc}")
        return 1
    print(json.dumps(plan, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
