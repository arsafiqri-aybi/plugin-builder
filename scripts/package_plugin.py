#!/usr/bin/env python3
"""Validate and create a deterministic ZIP containing one canonical plugin directory."""
import argparse, sys, zipfile
from pathlib import Path
from validate_plugin import validate

SKIP_PARTS={'.git','__pycache__','.pytest_cache','.mypy_cache'}
SKIP_NAMES={'.DS_Store'}

def package(root:Path,out:Path,public=False):
    root=root.resolve(); out=out.resolve()
    issues=validate(root,public)
    if issues: raise ValueError('validation failed:\n'+'\n'.join('- '+i for i in issues))
    out.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(x for x in root.rglob('*') if x.is_file() and not x.is_symlink()):
            rel=p.relative_to(root)
            if any(part in SKIP_PARTS for part in rel.parts) or p.name in SKIP_NAMES: continue
            zi=zipfile.ZipInfo((Path(root.name)/rel).as_posix(),date_time=(1980,1,1,0,0,0))
            zi.compress_type=zipfile.ZIP_DEFLATED; zi.external_attr=(0o100644<<16)
            z.writestr(zi,p.read_bytes())
    return out

def main():
    p=argparse.ArgumentParser(); p.add_argument('plugin_directory'); p.add_argument('--output',required=True); p.add_argument('--public',action='store_true'); a=p.parse_args()
    try: out=package(Path(a.plugin_directory),Path(a.output),a.public)
    except (ValueError,OSError) as e: print(f'package failed: {e}',file=sys.stderr); return 1
    print(out); return 0
if __name__=='__main__': raise SystemExit(main())
