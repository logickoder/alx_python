"""A simple square class that defines a method to print the itself"""


class Square:
    """Square class"""

    def __init__(self, size: int = 0):
        """__init__ method
        Args:
            size (int): size of the square
        """
        self.size = size

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

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
