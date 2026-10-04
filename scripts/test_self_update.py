#!/usr/bin/env python3
import unittest
from self_update_plan import plan

class SelfUpdateTests(unittest.TestCase):
    def test_forward_patch(self):
        p=plan("0.3.1","0.3.2","Add independent self-update layer")
        self.assertEqual(p["intent"],"self_update_plugin_builder")
        self.assertEqual(p["fallback_state"],"PACKAGE_READY")
        self.assertEqual(p["adapter_requirements"]["forbidden_dependency_name"],"Plugin Creator")

    def test_reject_same_version(self):
        with self.assertRaises(ValueError):
            plan("0.3.2","0.3.2","x")

    def test_reject_downgrade(self):
        with self.assertRaises(ValueError):
            plan("0.3.2","0.3.1","x")

    def test_reject_bad_semver(self):
        with self.assertRaises(ValueError):
            plan("0.3.1","next","x")

    def test_reject_empty_change(self):
        with self.assertRaises(ValueError):
            plan("0.3.1","0.3.2","   ")

if __name__=="__main__":
    unittest.main()
