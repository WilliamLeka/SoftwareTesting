from unittest import TestCase

from rectangle import Rectangle


class TestRectangle(TestCase):
    def setUp(self):
        # Create an instance of the Rectangle class for testing
        self.rectangle = Rectangle()

    def test_set_length(self):
        # Check if set_length sets length correctly
        self.rectangle.set_length(5)
        self.assertEqual(self.rectangle.get_length(), 5)

    def test_set_width(self):
        self.rectangle.set_width(10)
        self.assertEqual(self.rectangle.get_width(), 10)

    def test_reset(self):
        self.rectangle.set_length(5)
        self.rectangle.set_width(7)
        self.rectangle.reset()
        self.assertEqual(self.rectangle.get_length(), 0)
        self.assertEqual(self.rectangle.get_width(), 0)
        self.assertEqual(self.rectangle.get_area(), 0)

    def test_set_length_and_width(self):
        self.rectangle.set_length_and_width(3, 4)
        self.assertEqual(self.rectangle.get_length(), 3)
        self.assertEqual(self.rectangle.get_width(), 4)
        self.assertEqual(self.rectangle.get_area(), 12)

    def test_get_area(self):
        self.rectangle.set_length(6)
        self.rectangle.set_width(9)
        self.assertEqual(self.rectangle.get_area(), 54)

    def test_get_length(self):
        self.rectangle.set_length(5)
        self.assertEqual(self.rectangle.get_length(), 5)

    def test_get_width(self):
        self.rectangle.set_width(8)
        self.assertEqual(self.rectangle.get_width(), 8)

    def test_get_side_ratio(self):
        self.rectangle.set_length(6)
        self.rectangle.set_width(2)
        self.assertEqual(self.rectangle.get_side_ratio(), 3)

    def test_get_is_square(self):
        self.rectangle.set_length(4)
        self.rectangle.set_width(4)
        self.assertTrue(self.rectangle.get_is_square())
        self.rectangle.set_length(2)
        self.rectangle.set_width(4)
        self.assertFalse(self.rectangle.get_is_square())

    def test_rotate(self):
        self.rectangle.set_length(3)
        self.rectangle.set_width(5)
        self.rectangle.rotate()
        self.assertEqual(self.rectangle.get_length(), 5)
        self.assertEqual(self.rectangle.get_width(), 3)
