"""
A simple square class that inherits from Rectangle
"""

Rectangle = __import__("7-rectangle").Rectangle


class Square(Rectangle):
    """class that inherits from rectangle"""

    def __init__(self, size):
        """instantiation with size"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)
