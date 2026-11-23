import math


class Circle:
    """!Provides geometric calculations for a circle."""

    @staticmethod
    def area(r):
        """!Calculates the area of a circle.

        @param r Radius of the circle

        @return Area of the circle (pi * r^2)
        """
        return math.pi * r * r

    @staticmethod
    def perimeter(r):
        """!Calculates the perimeter of a circle.

        @param r Radius of the circle

        @return Perimeter of the circle (2 * pi * r)
        """
        return 2 * math.pi * r


class Rectangle:
    """!Provides geometric calculations for a rectangle."""

    @staticmethod
    def area(a, b):
        """!Calculates the area of a rectangle.

        @param a Length of one side
        @param b Length of the adjacent side

        @return Area of the rectangle (a * b)
        """
        return a * b

    @staticmethod
    def perimeter(a, b):
        """!Calculates the perimeter of a rectangle.

        @param a Length of one side
        @param b Length of the adjacent side

        @return Perimeter of the rectangle (2 * (a + b))
        """
        return 2 * (a + b)


class Square:
    """!Provides geometric calculations for a square."""

    @staticmethod
    def area(a):
        """!Calculates the area of a square.

        @param a Side length of the square

        @return Area of the square (a^2)
        """
        return a * a

    @staticmethod
    def perimeter(a):
        """!Calculates the perimeter of a square.

        @param a Side length of the square

        @return Perimeter of the square (4 * a)
        """
        return 4 * a


class Triangle:
    """!Provides geometric calculations for a triangle."""

    @staticmethod
    def area(a, h):
        """!Calculates the area of a triangle.

        @param a Base length of the triangle
        @param h Height of the triangle

        @return Area of the triangle (a * h / 2)
        """
        return a * h / 2

    @staticmethod
    def perimeter(a, b, c):
        """!Calculates the perimeter of a triangle.

        @param a Length of the first side
        @param b Length of the second side
        @param c Length of the third side

        @return Perimeter of the triangle (a + b + c)
        """
        return a + b + c
