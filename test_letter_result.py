import unittest

import letter_result

class MyTestCase(unittest.TestCase):

    def setUp(self):
       self.result = letter_result.LetterResult("A", "grey")
    def test_valid_input(self):
        self.assertEqual(self.result.letter, "A")
        self.assertEqual(self.result.colour, "grey")

    def test_invalid_letter(self):
        with self.assertRaises(ValueError):
            letter_result.LetterResult("AB", "grey")

    def test_only_letters(self):
        with self.assertRaises(ValueError):
            letter_result.LetterResult("43", "grey")

    def test_only_valid_colours(self):
        with self.assertRaises(ValueError):
            letter_result.LetterResult("A", "purple")




