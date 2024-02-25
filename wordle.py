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

        if Guessword.lower() == self.word.lower():
            return True
        else:
            self.guesses -= 1
            if self.guesses == 0:
                self.game_over = True
            return False

    def checkLetters(self, Guessword: str, pos: int):
        for letter in range(0,len(self.word)):
            if self.word[letter] == Guessword[pos]:


