#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=subprocess.run([sys.executable,str(root/'scripts/validate_neuron_map.py')],capture_output=True,text=True)
assert p.returncode==0, p.stdout+p.stderr
assert 'PASS' in p.stdout
text=(root/'SKILL.md').read_text(encoding='utf-8')
assert 'name: plugin-builder' in text
assert 'model is not an access-control boundary' in text.lower()
assert 'installation-adapters.md' in text
assert 'all 160 neurons' in text
print('Plugin Builder architecture tests: PASS')
