"""
The 6-rectangle module.
"""

BaseGeometry = __import__("5-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """instantiation with width and height"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
