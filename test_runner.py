import sublime
import sublime_plugin

import os
import unittest
import StringIO

from tests import test_parser
from tests import test_commands


class RunTestsCommand(sublime_plugin.WindowCommand):
    def is_enabled(self):
        return os.getcwd() == os.path.join(sublime.packages_path(), 'VintageEx')
        
    def run(self):
        bucket = StringIO.StringIO()
        suite = unittest.TestLoader().loadTestsFromModule(test_parser)
        # suite = unittest.TestLoader().loadTestsFromModule(test_commands)
        unittest.TextTestRunner(stream=bucket, verbosity=1).run(suite)

        v = self.window.new_file()
        edit = v.begin_edit()
        v.insert(edit, 0, bucket.getvalue())
        v.end_edit(edit)
        v.set_scratch(True)