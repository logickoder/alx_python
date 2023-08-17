"""A simple square class that defines an area method"""


class Square:
    """Square class"""

    def __init__(self, size: int = 0):
        """__init__ method
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> int:
        """Returns the area of the square"""
        return self.__size**2
