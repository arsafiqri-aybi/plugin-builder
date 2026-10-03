#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
issues=[]
files=sorted((ROOT/'knowledge').glob('[0-9][0-9]-*.md'))
if len(files)!=21: issues.append(f'expected 21 lobe files, found {len(files)}')
count=0
for f in files:
    text=f.read_text(encoding='utf-8')
    ns=re.findall(r'^###\s+(\d\d\.N[1-8])\s+—\s+.+$',text,re.M)
    count+=len(ns)
    if len(ns)!=8: issues.append(f'{f.name}: expected 8 neurons, found {len(ns)}')
    for label in ['**Decision model.**','**Failure signature.**','**Gate / evidence of mastery.**','**Synapses.**','**Primary sources.**']:
        if text.count(label)!=8: issues.append(f'{f.name}: {label} count={text.count(label)}')
if count!=168: issues.append(f'expected 168 neurons, found {count}')
required=['SKILL.md','README.md','NEURON_MAP.md','references/source-registry.md','references/build-workflow.md','references/security-gates.md','references/evaluation.md','references/architecture-search.md','references/installation-adapters.md','references/creator-parity-execution.md','evaluation/CREATOR_PARITY_MATRIX.md']
for p in required:
    if not (ROOT/p).is_file(): issues.append(f'missing {p}')
print('Plugin Builder neuron validation: '+('PASS' if not issues else 'FAIL'))
for i in issues: print('- '+i)
sys.exit(1 if issues else 0)
