"""A simple square class that defines a method to get the size and another to set it"""


class Square:
    """Square class"""

    def __init__(self, size: int = 0):
        """__init__ method
        Args:
            size (int): size of the square
        """
        Square.size = size

    def area(self) -> int:
        """Returns the area of the square"""
        return self.__size**2

    @property
    def size(self) -> int:
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value: int):
        """Sets the size of the square
        Args:
            value (int): size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
