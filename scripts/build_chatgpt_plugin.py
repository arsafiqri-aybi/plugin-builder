#!/usr/bin/env python3
"""Build the ChatGPT skills-only Plugin Builder package from canonical repo source."""

import argparse
import json
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RUNTIME_DIRS = ("knowledge", "references", "assets", "scripts", "agents")
RUNTIME_ROOT_FILES = ("SKILL.md", "NEURON_MAP.md")
SKIP_NAMES = {".DS_Store"}
SKIP_PARTS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache"}

def plugin_manifest(version: str) -> dict:
    return {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": "plugin-builder",
        "version": version,
        "description": (
            "Design, build, audit, validate, repair, create or update when supported, "
            "and evolve production-grade AI plugins from requirements through verified release."
        ),
        "author": {"name": "Arsafiqri Ummati Aybi"},
        "extensions": {
            "com.openai": {
                "interface": {
                    "displayName": "Plugin Builder",
                    "shortDescription": "Build excellent AI plugins",
                    "longDescription": (
                        "Plugin Builder is a specialist system for creating or improving AI plugins. "
                        "It performs requirement modeling, architecture search, Skill/MCP/tool/UI design, "
                        "authentication and authorization design, security and side-effect analysis, "
                        "deterministic package validation, creator-parity lifecycle execution, adversarial and behavioral evaluation, repair, "
                        "versioned packaging, and host-aware install/update verification without inventing "
                        "capabilities or evidence."
                    ),
                    "developerName": "Arsafiqri Ummati Aybi",
                    "category": "Developer Tools",
                    "capabilities": ["Interactive"],
                    "defaultPrompt": [
                        "Build the best plugin for this requirement.",
                        "Audit and improve this plugin.",
                        "Design, test, and install this plugin when the host supports it."
                    ]
                }
            }
        }
    }

def keep_runtime_file(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in SKIP_PARTS for part in rel.parts) or path.name in SKIP_NAMES:
        return False
    if path.name.endswith(".pyc"):
        return False
    return True

def copy_runtime(stage: Path):
    skill = stage / "skills" / "plugin-builder"
    skill.mkdir(parents=True, exist_ok=True)

    for name in RUNTIME_ROOT_FILES:
        src = ROOT / name
        if not src.is_file():
            raise FileNotFoundError(src)
        shutil.copy2(src, skill / name)

    for dirname in RUNTIME_DIRS:
        src_dir = ROOT / dirname
        if not src_dir.is_dir():
            continue
        for src in src_dir.rglob("*"):
            if not src.is_file() or not keep_runtime_file(src):
                continue
            rel = src.relative_to(src_dir)
            dst = skill / dirname / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    # Keep comparative evaluation in the runtime package as evidence protocol,
    # while avoiding engineering-only status/docs/CI files.
    for eval_name in ("BUILDER_BENCHMARK.md", "CREATOR_PARITY_MATRIX.md"):
        src = ROOT / "evaluation" / eval_name
        if src.is_file():
            dst = skill / "evaluation" / eval_name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

def write_zip(stage: Path, output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for src in sorted(p for p in stage.rglob("*") if p.is_file()):
            rel = src.relative_to(stage)
            arc = Path(stage.name) / rel
            zi = zipfile.ZipInfo(arc.as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o100644 << 16
            z.writestr(zi, src.read_bytes())

def build(version: str, output: Path):
    with tempfile.TemporaryDirectory(prefix="plugin-builder-chatgpt-") as td:
        stage = Path(td) / "plugin-builder"
        stage.mkdir(parents=True)
        (stage / "plugin.json").write_text(
            json.dumps(plugin_manifest(version), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        copy_runtime(stage)
        write_zip(stage, output)
    return output

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--version", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    out = build(a.version, Path(a.output).resolve())
    print(out)

if __name__ == "__main__":
    main()
