class Rectangle:

    def __init__(self, length=None, width=None):
        """
        Constructor: Usage=Rectangle(width, length)
                creates a rectangle with width and length as specified by parameters.
                Width and length should be numeric values.
        :param length: the length of the rectangle (number)
        :param width: the width of the rectangle (number)
        """
        self.length = length if length is not None else 0
        self.width = width if width is not None else 0
        self.area = self.length * self.width
        self.is_square = self.length == self.width

    def set_length(self, length):
        """
        Set the length of the rectangle
        :param length: length of the rectangle
        :return: None
        """
        self.length = length
        self.area = self.length * self.width
        self.is_square = self.length == self.width

    def set_width(self, width):
        """
        Set the width of the rectangle
        :param width:
        :return: None
        """
        self.width = width
        self.area = self.length * self.width
        self.is_square = self.length == self.width

    def reset(self):
        """
        Reset the rectangle
        :return: None
        """
        self.length = 0
        self.width = 0
        self.area = 0

    def set_length_and_width(self, length, width):
        """
        Set the length and width together, this saves you having to call setLength and setWidth directly
        :param length: length of the rectangle
        :param width: width of the rectangle
        :return: None
        """
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def get_area(self):
        """
        Get the area of the rectangle (length x width)
        :return: area of the rectangle: Number
        """
        return self.area

    def get_length(self):
        """
        Get the length of the rectangle
        :return: length: Number
        """
        return self.length

    def get_width(self):
        """
        Get the width of the rectangle
        :return: width: Number
        """
        return self.width

    def get_side_ratio(self):
        """
        Get the ratio of the width of the rectangle to the length of the rectangle (width / length)
        :return: ratio: Number
        """
        return self.length / self.width

    def get_is_square(self):
        """
        Get a boolean representing whether this rectangle is a square (length is equal to width)
        :return: is_square: Boolean
        """
        return self.is_square

    def rotate(self):
        """
        Rotate this rectangle (length becomes width and width becomes length)
        :return: None
        """
        # rotate the rectangle by swapping width and length
        temp = self.length
        self.length = self.width
        self.width = temp
