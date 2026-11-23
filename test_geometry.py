import math
import unittest

from geometry import Circle, Rectangle, Square, Triangle


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(Circle.area(0), 0)

    def test_area_standard(self):
        self.assertAlmostEqual(Circle.area(3), math.pi * 9)

    def test_area_float(self):
        self.assertAlmostEqual(Circle.area(2.5), math.pi * 6.25)

    def test_perimeter_zero(self):
        self.assertEqual(Circle.perimeter(0), 0)

    def test_perimeter_standard(self):
        self.assertAlmostEqual(Circle.perimeter(3), 2 * math.pi * 3)

    def test_perimeter_float(self):
        self.assertAlmostEqual(Circle.perimeter(2.5), 2 * math.pi * 2.5)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(Rectangle.area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(Rectangle.area(10, 10), 100)

    def test_area_standard(self):
        self.assertEqual(Rectangle.area(3, 7), 21)

    def test_area_float(self):
        self.assertAlmostEqual(Rectangle.area(2.5, 4.2), 10.5)

    def test_perimeter_zero(self):
        self.assertEqual(Rectangle.perimeter(0, 0), 0)

    def test_perimeter_standard(self):
        self.assertEqual(Rectangle.perimeter(3, 7), 20)

    def test_perimeter_float(self):
        self.assertAlmostEqual(Rectangle.perimeter(1.5, 2.5), 8.0)


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(Square.area(0), 0)

    def test_area_standard(self):
        self.assertEqual(Square.area(5), 25)

    def test_area_float(self):
        self.assertAlmostEqual(Square.area(2.5), 6.25)

    def test_perimeter_zero(self):
        self.assertEqual(Square.perimeter(0), 0)

    def test_perimeter_standard(self):
        self.assertEqual(Square.perimeter(5), 20)

    def test_perimeter_float(self):
        self.assertAlmostEqual(Square.perimeter(2.5), 10.0)


class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(Triangle.area(10, 0), 0)

    def test_area_standard(self):
        self.assertEqual(Triangle.area(10, 5), 25.0)

    def test_area_float(self):
        self.assertAlmostEqual(Triangle.area(3.5, 2.0), 3.5)

    def test_perimeter_zero(self):
        self.assertEqual(Triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_standard(self):
        self.assertEqual(Triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_float(self):
        self.assertAlmostEqual(Triangle.perimeter(1.5, 2.5, 3.0), 7.0)


if __name__ == "__main__":
    unittest.main()
