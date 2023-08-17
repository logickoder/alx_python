"""
BaseGeometry class
"""


from collections.abc import Iterable


class BaseGeometry:
    """BaseGeometry class"""

    def __dir__(self) -> Iterable[str]:
        """Returns the list of available attributes and methods of an object"""
        """Remove __init_subclass__ from the list"""
        return [item for item in dir(self) if item != "__init_subclass__"]
