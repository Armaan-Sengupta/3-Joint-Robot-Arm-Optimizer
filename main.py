import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y   

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def toString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.angle = self.get_angle();

    def get_length(self):
        return math.sqrt((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)
    
    def get_angle(self):
        return math.atan2(self.p2.y - self.p1.y, self.p2.x - self.p1.x)

    def set_length(self, length):
        self.p2.x = self.p1.x + length * self.get_slope()
        self.p2.y = self.p1.y + length

    # make a function to update point 2 based on the angle and length
    def set_angle(self, angle):
        self.p2.x = self.p1.x + self.get_length() * math.cos(angle)
        self.p2.y = self.p1.y + self.get_length() * math.sin(angle)

    def toString(self):
        return "Line: " + self.p1.toString() + " to " + self.p2.toString()

    def start(self):
        return self.p1
    def end(self):
        return self.p2


