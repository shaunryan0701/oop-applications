from rectangle import Rectangle
from point import Point
from random import randint

upperright = Point(randint(10, 19), randint(10, 19))
lowerleft = Point(randint(0, 9), randint(0, 9))

rectangle = Rectangle(lowerleft=lowerleft, upperright=upperright)

point1 = Point(randint(0, 19), randint(0, 19))
print("Rectangle co-ordinates:", rectangle.lowerleft.x, rectangle.lowerleft.y, "and", rectangle.upperright.x, rectangle.upperright.y)
print("Rectangle area:", rectangle.area(), "units squared")
print("Guessed point:", point1.x, point1.y)
print("Point in rectangle?:", point1.falls_in_rectangle(rectangle))
