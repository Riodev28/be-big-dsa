import ast
from .value_objects.normalized_code import NormalizedCode
from ...core import ParseTreeError, CodeNotNormalizedError


class Parser:
    @staticmethod
    def to_tree_node(code: NormalizedCode):
        """Parse code to a AST tree node"""
        Parser._validate_code(code)

        try:
            return ast.parse(code.value())
        except SyntaxError as e:
            raise ParseTreeError(f"Error parsing code: {e}") from e

    @staticmethod
    def _validate_code(code: NormalizedCode) -> None:
        """Validate code param before parse it"""
        if not isinstance(code, NormalizedCode):
            raise CodeNotNormalizedError("Code must be normalized first")
