#
import letter_result
class Wordle:

    def __init__(self, word: str, valid_words: list):
        self.game_over = False
        self.guesses = 6
        self.valid_words = valid_words
        if len(word) == 5:
            self.word = word
        else:
            raise ValueError("Word is not exactly 5 characters long")

    def guess(self, Guessword : str):
        guessValid = False
        for word in self.valid_words:
            if Guessword == word:
                guessValid = True

        if guessValid == False:
            raise ValueError(Guessword + " is not a valid word")

        letters = self.checkLetters(Guessword)

        if Guessword.lower() == self.word.lower():
            return letters
        else:
            self.guesses -= 1
            if self.guesses == 0:
                self.game_over = True
            return letters

    def checkLetters(self, Guessword : str):
        results = []
        for i in range(len(self.word)):
            guessed_letter = Guessword[i]
            actual_letter = self.word[i]

            if guessed_letter == actual_letter:
                results.append(letter_result.LetterResult(guessed_letter, "green"))
            elif guessed_letter in self.word:
                results.append(letter_result.LetterResult(guessed_letter, "yellow"))
            else:
                results.append(letter_result.LetterResult(guessed_letter, "grey"))
        return results

