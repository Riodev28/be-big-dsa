import ast

class AllocationVisitors(ast.NodeVisitor):
    def __init__(self):
        self.list_allocations = 0
        
    def visit_List(self, node):
        """ Visit declared lists in the algorithm """
        self.list_allocations += 1
        self.generic_visit(node)