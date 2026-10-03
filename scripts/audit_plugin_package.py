#!/usr/bin/env python3
import json,re,sys
from pathlib import Path

def audit(path):
    root=Path(path)
    issues=[]
    manifest=root/'plugin.json'
    if not manifest.is_file():
        return ['plugin.json missing']
    try: data=json.loads(manifest.read_text(encoding='utf-8'))
    except Exception as e: return [f'plugin.json invalid JSON: {e}']
    if data.get('$schema')!='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json': issues.append('unexpected or missing Agent Plugins 1.0 schema')
    name=data.get('name')
    if not isinstance(name,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name) or len(name)>64: issues.append('invalid plugin name')
    ver=data.get('version')
    if not isinstance(ver,str) or not re.fullmatch(r'\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?',ver): issues.append('version is not strict semantic form')
    for p in root.rglob('*'):
        if p.is_symlink(): issues.append(f'symlink not allowed in audit: {p.relative_to(root)}')
        if p.is_file() and p.stat().st_size<2_000_000:
            try: txt=p.read_text(encoding='utf-8',errors='strict')
            except Exception: continue
            if re.search(r'(?i)(api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*["\']?[A-Za-z0-9_\-]{16,}',txt): issues.append(f'possible secret in {p.relative_to(root)}')
    for skill in (root/'skills').glob('*/SKILL.md') if (root/'skills').is_dir() else []:
        t=skill.read_text(encoding='utf-8')
        if not t.startswith('---\n'): issues.append(f'invalid skill frontmatter: {skill.relative_to(root)}')
    return issues

if __name__=='__main__':
    if len(sys.argv)!=2: print('usage: audit_plugin_package.py <plugin-dir>'); sys.exit(2)
    issues=audit(sys.argv[1])
    print('Static plugin audit: '+('PASS' if not issues else 'FAIL'))
    for i in issues: print('- '+i)
    sys.exit(1 if issues else 0)
