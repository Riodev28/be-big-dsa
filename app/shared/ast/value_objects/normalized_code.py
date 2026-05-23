import black
from ....core import NormalizeCodeError

class NormalizedCode:
    def __init__(self, code: str):
        self.code = self.__normalize(code)
        
    @staticmethod
    def __normalize(code: str) -> str:
        """ Normalize code """
        try:
            return black.format_str(code, mode=black.Mode())
        except black.InvalidInput:
            raise NormalizeCodeError("Invalid Python code")
        
    def value(self) -> str:
        """ Return normalized value as a string """
        return self.code