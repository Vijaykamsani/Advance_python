"""
homework-3
Problem -1
 vijay kumar Kamsani
"""


# Creating a class Point that represents an (x-y) coordinate pair and provides x and y read-write properties

class Point:

    def __init__(self):
        self._y = None
        self._x = None

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def x(self, value):
        self._x = value

    def y(self):
        return self._y

    def y(self, value):
        self._y = value

    def move(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x},{self._y})"


# Creating  a class Circle that has its non-public attributes
class Circle:
    def __init__(self, radius, point):
        self._radius = radius
        self._point = point

    # a move method that receives x- and y-coordinate values and sets a new location
    def move(self, x, y):
        self._point.move(x, y)

    # Displaying its string representation,
    def __str__(self=None):
        return f"A circle with  radius of {self._radius} and center point {self._point}"


# main function to run the file
if __name__ == '__main__':
    p1 = Point(0, 0)
    c1 = Circle(1, p1)
    print("Before the move")
    print(c1)
    c1.move(1, 1)
    print("After the move")
    print(c1)
