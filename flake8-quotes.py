import ast

from flake8 import reporter
from flake8.checker import Checker
from flake8.plugins.manager import Plugin

class NoDoubleQuotes(Plugin):
    name = 'flake8-no-double-quotes'
    version = '1.0.0'
    codemap = {
        'DOUBLE_QUOTES': ('DQ000', 'Avoid using double quotes')
    }

    def visit_Str(self, node):
        # Check if the string is surrounded by double quotes
        if isinstance(node.s, str) and node.s.startswith('"') and node.s.endswith('"'):
            self.error(node, 'DQ000')
        
    @classmethod
    def parse_options(cls, options):
        # Parse options and extract plugin-specific options
        pass
        
    @classmethod
    def add_options(cls, parser):
        # Add plugin-specific options to the parser
        pass
        
    @classmethod
    def run(cls, tree, filename, lines, options, state):
        # Create a checker instance and run the visitor on the AST
        checker = NoDoubleQuotes(None, filename, lines, options, state, reporter)
        checker.visit(tree)
