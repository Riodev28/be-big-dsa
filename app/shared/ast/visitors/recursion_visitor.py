import ast


class RecursionVisitors(ast.NodeVisitor):
    def __init__(self):
        self.current_function = None
        self.recursive_functions = set()

    def visit_FunctionDef(self, node):
        """Visit functions/def statements and control the previous function and the current"""
        previous = self.current_function
        self.current_function = node.name

        self.generic_visit(node)

        self.current_function = previous

    def visit_Call(self, node):
        """Visit call methods and count how many recursive functions exists"""
        if isinstance(node.func, ast.Name) and node.func.id == self.current_function:
            self.recursive_functions.add(self.current_function)

        self.generic_visit(node)
