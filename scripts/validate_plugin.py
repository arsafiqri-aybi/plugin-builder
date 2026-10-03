#!/usr/bin/env python3
"""Deterministic validator for portable Plugin Builder output."""
import argparse, json, re
from pathlib import Path

NAME_RE=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
SEMVER_RE=re.compile(r'^(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$')
SECRET_NAME_RE=re.compile(r'(^|/)(\.env(?:\..*)?|id_rsa|id_ed25519|credentials\.json|service-account.*\.json)$',re.I)
SECRET_TEXT_RE=re.compile(r'(?i)(api[_-]?key|access[_-]?token|client[_-]?secret|private[_-]?key)\s*[:=]\s*["\']?[A-Za-z0-9_\-/+=]{16,}')

def parse_json(path,issues,label):
    try: return json.loads(path.read_text(encoding='utf-8'))
    except Exception as e: issues.append(f'{label}: invalid JSON: {e}'); return None

def parse_frontmatter(text):
    if not text.startswith('---\n'): return None
    end=text.find('\n---\n',4)
    if end<0: return None
    data={}
    for line in text[4:end].splitlines():
        if ':' in line:
            k,v=line.split(':',1); data[k.strip()]=v.strip().strip('"\'')
    return data

def validate(root:Path,public=False):
    root=root.resolve(); issues=[]
    mf=root/'plugin.json'
    if not mf.is_file(): return ['plugin.json missing']
    data=parse_json(mf,issues,'plugin.json')
    if data:
        if data.get('$schema')!='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json': issues.append('plugin.json: unexpected/missing Agent Plugins 1.0 schema')
        name=data.get('name'); version=data.get('version'); desc=data.get('description')
        if not isinstance(name,str) or not NAME_RE.fullmatch(name) or len(name)>64: issues.append('plugin.json: invalid name')
        if not isinstance(version,str) or not SEMVER_RE.fullmatch(version): issues.append('plugin.json: invalid semantic version')
        if not isinstance(desc,str) or not desc.strip(): issues.append('plugin.json: description required')
        ext=((data.get('extensions') or {}).get('com.openai') or {}) if isinstance(data.get('extensions') or {},dict) else {}
        interface=ext.get('interface') or {}
        for key in ('logo','composerIcon','logoDark','composerIconDark'):
            val=interface.get(key) if isinstance(interface,dict) else None
            if val:
                p=(root/val).resolve()
                if root not in p.parents or not p.is_file(): issues.append(f'plugin.json: {key} path missing/outside package: {val}')
        if public:
            if (root/'.app.json').exists(): issues.append('public package: root .app.json is not allowed')
            if ext.get('apps') is not None: issues.append('public package: extensions.com.openai.apps must be absent/null')
    for p in root.rglob('*'):
        rel=p.relative_to(root).as_posix()
        if p.is_symlink(): issues.append(f'symlink not allowed: {rel}'); continue
        if p.is_file():
            if SECRET_NAME_RE.search('/'+rel): issues.append(f'possible secret file: {rel}')
            if p.stat().st_size<=2_000_000:
                try: txt=p.read_text(encoding='utf-8')
                except Exception: txt=''
                if SECRET_TEXT_RE.search(txt): issues.append(f'possible embedded secret: {rel}')
    skills=root/'skills'
    if skills.is_dir():
        for d in sorted(p for p in skills.iterdir() if p.is_dir()):
            sf=d/'SKILL.md'
            if not sf.is_file(): issues.append(f'skill missing SKILL.md: {d.name}'); continue
            fm=parse_frontmatter(sf.read_text(encoding='utf-8'))
            if not fm: issues.append(f'invalid skill frontmatter: skills/{d.name}/SKILL.md'); continue
            if fm.get('name')!=d.name: issues.append(f'skill name/folder mismatch: {d.name}')
            if not fm.get('description','').strip(): issues.append(f'skill description missing: {d.name}')
    mcp=root/'mcp.json'
    if mcp.is_file():
        m=parse_json(mcp,issues,'mcp.json')
        if m:
            if m.get('$schema')!='https://agent-plugins.org/schemas/1.0.0/mcp.schema.json': issues.append('mcp.json: unexpected/missing schema')
            servers=m.get('mcpServers')
            if not isinstance(servers,dict) or not servers: issues.append('mcp.json: mcpServers must be a non-empty object')
            else:
                for n,cfg in servers.items():
                    if not isinstance(cfg,dict): issues.append(f'mcp.json: {n} config must be object'); continue
                    typ=cfg.get('type')
                    if typ=='streamable-http':
                        if not isinstance(cfg.get('url'),str) or not cfg['url'].startswith('https://'): issues.append(f'mcp.json: {n} remote URL must use https://')
                    elif typ=='stdio':
                        if not isinstance(cfg.get('command'),str) or not cfg['command'].strip(): issues.append(f'mcp.json: {n} stdio command required')
                    else: issues.append(f'mcp.json: {n} unsupported/missing type')
    overlay=root/'.codex-plugin'/'plugin.json'
    if overlay.is_file() and data:
        ov=parse_json(overlay,issues,'.codex-plugin/plugin.json')
        if ov:
            for k in ('name','version'):
                if ov.get(k) is not None and ov.get(k)!=data.get(k): issues.append(f'compatibility overlay {k} differs from root manifest')
    return issues

def main():
    p=argparse.ArgumentParser(); p.add_argument('plugin_directory'); p.add_argument('--public',action='store_true'); a=p.parse_args()
    issues=validate(Path(a.plugin_directory),a.public)
    print('Plugin validation: '+('PASS' if not issues else 'FAIL'))
    for i in issues: print('- '+i)
    return 1 if issues else 0
if __name__=='__main__': raise SystemExit(main())
