#!/usr/bin/env python3
"""Build a safe self-update execution plan for Plugin Builder.

This script never mutates ChatGPT account state. It validates intent and emits
an adapter-neutral plan that the runtime may execute with real host capabilities.
"""
import argparse
import json
import re

SEMVER_RE=re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")

def parse_version(v:str):
    m=SEMVER_RE.fullmatch(v.strip())
    if not m:
        raise ValueError("target_version must be semantic version")
    return tuple(int(m.group(i)) for i in range(1,4))

def plan(current_version:str,target_version:str,change:str,repo:str="arsafiqri-aybi/plugin-builder"):
    cur=parse_version(current_version)
    tar=parse_version(target_version)
    if tar<=cur:
        raise ValueError("target_version must be greater than current_version")
    if not change.strip():
        raise ValueError("change description is required")
    return {
      "intent":"self_update_plugin_builder",
      "canonical_source":{"kind":"git","repository":repo},
      "current_version":current_version,
      "target_version":target_version,
      "change":change.strip(),
      "phases":[
        "resolve_identity_and_current_release",
        "freeze_known_good_commit_and_release",
        "edit_canonical_source",
        "run_static_and_regression_tests",
        "build_deterministic_candidate_archive",
        "inspect_candidate_archive",
        "discover_generic_host_update_adapter",
        "guarded_update_if_available",
        "read_back_release_and_critical_files",
        "smoke_verify_and_report_exact_state"
      ],
      "adapter_requirements":{
        "must_update_exact_owned_plugin":True,
        "must_accept_archive_or_equivalent_release_artifact":True,
        "must_support_or_emulate_release_guard":True,
        "must_allow_read_back":True,
        "forbidden_dependency_name":"Plugin Creator"
      },
      "fallback_state":"PACKAGE_READY",
      "installed_success_state":"INSTALLED_VERIFIED"
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--current-version",required=True)
    p.add_argument("--target-version",required=True)
    p.add_argument("--change",required=True)
    p.add_argument("--repo",default="arsafiqri-aybi/plugin-builder")
    a=p.parse_args()
    try:
        result=plan(a.current_version,a.target_version,a.change,a.repo)
    except ValueError as e:
        print(f"self-update plan failed: {e}")
        return 1
    print(json.dumps(result,indent=2,ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
