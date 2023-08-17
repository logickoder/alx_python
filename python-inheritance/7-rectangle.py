"""
    A simple rectangle class that inherits from BaseGeometry
"""
BaseGeometry = __import__("5-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a sub-class of the baseclass
    """

    def __init__(self, width, height):
        """
        function sets the values width and height and ensures
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
