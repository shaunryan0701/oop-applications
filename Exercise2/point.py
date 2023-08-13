import math

class Point:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowerleft, upperright):
        if lowerleft.x < self.x < upperright.x and \
            lowerleft

    def distance(self, point):
        x_diff = self.x - point.x
        y_diff =  self.y - point.y
        # ** 0.5 is raising a number to the 1/2 power or sqrt
        return ((x_diff) **2  + (y_diff)**2) ** 0.5
    
point1 = Point(0, 0)
point2 = Point(30, 40)

print(point2.distance(point1))
