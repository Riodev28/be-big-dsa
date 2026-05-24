import hashlib
from .value_objects.normalized_code import NormalizedCode


class Fingerprint:
    def __init__(self, code: NormalizedCode):
        self.value = code

    @staticmethod
    def _hash(code: NormalizedCode) -> str:
        """Hash code"""
        return hashlib.sha256(code.value().encode()).hexdigest()

    def digest(self) -> str:
        """Return code hashed"""
        return Fingerprint._hash(self.value)
