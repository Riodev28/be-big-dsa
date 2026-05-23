import ast


class LoopVisitors(ast.NodeVisitor):
    def __init__(self):
        self.max_depth = 0
        self.current_depth = 0

    def visit_For(self, node):
        """Visit a for loop and get a counter of max depth
        (how many for loops there are inside the another one)"""

        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1

    def visit_While(self, node):
        """Visit a while loop and get a counter of max depth
        (how many while loops there are inside the another one)"""

        self.current_depth += 1
        self.max_depth = max(self.max_depth, self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1
