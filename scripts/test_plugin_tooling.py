#!/usr/bin/env python3
import argparse, tempfile, unittest, zipfile
from pathlib import Path
from init_plugin import create
from validate_plugin import validate
from package_plugin import package

class T(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup); self.base=Path(self.tmp.name)
    def args(self,**kw):
        d=dict(name='Example Plugin',path=str(self.base),description='Provide a safe example workflow.',author='Example',skill='example-workflow',skill_description='Use for the example workflow.',mcp_url=[],assets=False)
        d.update(kw); return argparse.Namespace(**d)
    def test_scaffold_validate_package(self):
        root=create(self.args(mcp_url=['example=https://example.com/mcp']))
        self.assertEqual(validate(root),[])
        out=self.base/'out.zip'; package(root,out)
        with zipfile.ZipFile(out) as z:
            names=z.namelist()
            self.assertIn('example-plugin/plugin.json',names)
            self.assertIn('example-plugin/skills/example-workflow/SKILL.md',names)
            self.assertIn('example-plugin/mcp.json',names)
    def test_secret_file_is_rejected(self):
        root=create(self.args()); key='API'+'_'+'KEY'; (root/'.env').write_text(key+'='+'a'*24,encoding='utf-8')
        self.assertTrue(any('secret' in x for x in validate(root)))
    def test_public_app_binding_rejected(self):
        root=create(self.args()); (root/'.app.json').write_text('{}',encoding='utf-8')
        self.assertTrue(any('public package' in x for x in validate(root,public=True)))

if __name__=='__main__': unittest.main()
