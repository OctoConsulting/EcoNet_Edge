class Detect:
    def __init__(self, x1, y1, x2, y2, label, score=-1):
        """
        Represents a single box (ground truth or inference result)
        """
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._label = label
        self._score = score

    @property
    def x1(self):
        return self._x1

    @property
    def y1(self):
        return self._y1

    @property
    def x2(self):
        return self._x2

    @property
    def y2(self):
        return self._y2

    @property
    def label(self):
        return self._label

    @property
    def score(self):
        return self._score

    @property
    def height(self):
        return self._y2 - self._y1

    @property
    def width(self):
        return self._x2 - self._x1

    @x1.setter
    def x1(self, x1):
        self._x1 = x1

    @y1.setter
    def y1(self, y1):
        self._y1 = y1

    @x2.setter
    def x2(self, x2):
        self._x2 = x2

    @y2.setter
    def y2(self, y2):
        self._y2 = y2

    @label.setter
    def label(self, label):
        self._label = label

    @score.setter
    def score(self, score):
        self._score = score
