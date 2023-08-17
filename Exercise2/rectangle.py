from point import Point

class Rectangle:
    
    def __init__(self, lowerleft: Point, upperright: Point):
        self.lowerleft = lowerleft
        self.upperright = upperright

    def area(self):
        return (self.upperright.x - self.lowerleft.x) * \
        (self.upperright.y - self.lowerleft.y)
