import unittest

from wordle import Wordle


class TestWordle(unittest.TestCase):

    def setUp(self):
        self.valid_words = ["kites", "chart", "crane", "gnoll", "cream", "throw", "glass", "bread", "great"]
        self.game = Wordle("great", self.valid_words)
    def test_constructor_only_allows_five_letter_words(self):

        self.assertRaises(ValueError, Wordle, "good", self.valid_words)  # 4 letters, should fail
        self.assertRaises(ValueError, Wordle, "better", self.valid_words)  # 6 letters, should fail

    def test_user_is_allowed_six_guesses(self):
        guess_words = ["kites", "chart", "crane", "gnoll", "cream", "throw"]

        for word in guess_words:
            self.assertFalse(self.game.game_over, msg="Game should allow up to six guesses")
            self.game.guess(word)

        self.assertTrue(self.game.game_over, msg="Game should end after six guesses")

    def test_only_dictionary_words_allowed(self):
        self.game.guess("kites")
        self.assertRaises(ValueError, self.game.guess, "abcde")

    def test_guess_returns_a_list_of_letter_results(self):
        result = self.game.guess("glass")
        self.assertTrue(5, len(result))
        first_letter = result[0]
        self.assertEqual("g", first_letter.letter)
        self.assertIsNotNone(first_letter.colour)
