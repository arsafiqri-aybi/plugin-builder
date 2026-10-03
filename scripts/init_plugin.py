#!/usr/bin/env python3
"""Create a minimal portable Agent Plugins package from explicit components."""
import argparse, json, re, sys
from pathlib import Path

NAME_RE=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')

def normalize(v:str)->str:
    v=re.sub(r'[^a-z0-9]+','-',v.strip().lower())
    return re.sub(r'-+','-',v).strip('-')

def parse_mcp(items):
    servers={}
    for item in items or []:
        if '=' not in item: raise ValueError('--mcp-url must be NAME=https://host/path')
        name,url=item.split('=',1); name=normalize(name); url=url.strip()
        if not NAME_RE.fullmatch(name): raise ValueError(f'invalid MCP server name: {name}')
        if not url.startswith('https://'): raise ValueError('remote MCP URL must use https://')
        servers[name]={'type':'streamable-http','url':url}
    return servers

def create(args):
    name=normalize(args.name)
    if not NAME_RE.fullmatch(name) or len(name)>64: raise ValueError('invalid plugin name')
    if not args.description.strip(): raise ValueError('description is required')
    target=Path(args.path).resolve()/name
    if target.exists(): raise FileExistsError(f'target exists: {target}')
    target.mkdir(parents=True)
    manifest={
      '$schema':'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json',
      'name':name,'version':'0.1.0','description':args.description.strip(),
      'author':{'name':args.author.strip()}
    }
    (target/'plugin.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    if args.skill:
        sname=normalize(args.skill)
        if not NAME_RE.fullmatch(sname): raise ValueError('invalid skill name')
        sd=(target/'skills'/sname); sd.mkdir(parents=True)
        desc=(args.skill_description or f'Use this skill for {args.description.strip()}').strip()
        (sd/'SKILL.md').write_text(f'---\nname: {sname}\ndescription: {desc}\n---\n\n# {sname.replace("-"," ").title()}\n\nDefine the workflow, boundaries, failure handling, and completion evidence.\n',encoding='utf-8')
    servers=parse_mcp(args.mcp_url)
    if servers:
        (target/'mcp.json').write_text(json.dumps({'$schema':'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json','mcpServers':servers},indent=2)+'\n',encoding='utf-8')
    if args.assets: (target/'assets').mkdir()
    return target

def main():
    p=argparse.ArgumentParser()
    p.add_argument('name'); p.add_argument('--path',required=True); p.add_argument('--description',required=True); p.add_argument('--author',required=True)
    p.add_argument('--skill'); p.add_argument('--skill-description'); p.add_argument('--mcp-url',action='append',default=[]); p.add_argument('--assets',action='store_true')
    a=p.parse_args()
    try: target=create(a)
    except (ValueError,OSError) as e: print(f'init failed: {e}',file=sys.stderr); return 1
    print(target); return 0
if __name__=='__main__': raise SystemExit(main())
