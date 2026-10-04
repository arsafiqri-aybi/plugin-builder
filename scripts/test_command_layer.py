#!/usr/bin/env python3
import unittest
from command_layer import parse_command

class CommandLayerTests(unittest.TestCase):
    def test_minimal_create_personal_plugin(self):
        p=parse_command('create_personal_plugin(mcp_url="https://github-write-bridge.example.workers.dev/mcp")')
        self.assertEqual(p["intent"],"create_private_plugin_from_existing_remote_mcp")
        self.assertEqual(p["plugin"]["name"],"github-write-bridge")
        self.assertEqual(p["source"]["transport"],"streamable-http")
        self.assertEqual(p["fallback_state"],"PACKAGE_READY")

    def test_explicit_metadata(self):
        p=parse_command('create_personal_plugin(mcp_url="https://mcp.example.com/mcp", name="my-plugin", display_name="My Plugin", description="GitHub bridge", author="Example Author")')
        self.assertEqual(p["plugin"]["name"],"my-plugin")
        self.assertEqual(p["plugin"]["author"],"Example Author")

    def test_reject_http(self):
        with self.assertRaises(ValueError):
            parse_command('create_personal_plugin(mcp_url="http://example.com/mcp")')

    def test_reject_credentials(self):
        with self.assertRaises(ValueError):
            parse_command('create_personal_plugin(mcp_url="https://user:pass@example.com/mcp")')

    def test_reject_unknown_argument(self):
        with self.assertRaises(ValueError):
            parse_command('create_personal_plugin(mcp_url="https://example.com/mcp", token="secret")')

    def test_reject_code_execution(self):
        with self.assertRaises(ValueError):
            parse_command('create_personal_plugin(mcp_url=__import__("os").getcwd())')

    def test_self_update_alias(self):
        p=parse_command('self_update_plugin_builder(target_version="0.3.2", change="Add independent self-update lifecycle")')
        self.assertEqual(p["intent"],"self_update_plugin_builder")
        self.assertEqual(p["target_version"],"0.3.2")
        self.assertEqual(p["forbidden_dependency"],"Plugin Creator")
        self.assertEqual(p["fallback_state"],"PACKAGE_READY")

    def test_self_update_rejects_bad_version(self):
        with self.assertRaises(ValueError):
            parse_command('self_update_plugin_builder(target_version="next", change="x")')

if __name__=="__main__":
    unittest.main()
