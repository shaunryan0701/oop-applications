class Point:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowerleft.x < self.x < rectangle.upperright.x and \
            rectangle.lowerleft.y < self.y < rectangle.upperright.y:
            return True
        else:
            return False

    def distance(self, point):
        x_diff = self.x - point.x
        y_diff =  self.y - point.y
        # ** 0.5 is raising a number to the 1/2 power or sqrt
        return ((x_diff) **2  + (y_diff)**2) ** 0.5
    
