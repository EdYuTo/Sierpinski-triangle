class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str("(" + str(self.x) + ", " + str(self.y) + ")")

    def __repr__(self):
        return str(self)
    
    def midPoint(self, other):
        return Point((self.x+other.x)/2, (self.y+other.y)/2)
