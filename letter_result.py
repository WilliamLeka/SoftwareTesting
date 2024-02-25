class LetterResult:
    letter: str = None
    colour: str = None
    valid_colours = ["grey", "yellow", "green"]

    def __init__(self, letter: str, colour: str):
        if len(letter) > 1 or letter.isalpha() == False:
            raise ValueError("Only one letter allowed")
        self.letter = letter

        for Validcolour in self.valid_colours:
            if Validcolour == colour:
                self.colour = colour
        if self.colour is None:
            raise ValueError("A valid colour must be entered")

    def changeColour(self, colour: str):
        self.colour = colour

    def __str__(self):
        return f'{self.letter} ({self.colour})'
