class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    # def __repr__(self):
    #     return "{}{}".format(self.__class__.__name__, self)


p = Point(3, 6)

print(p)