class Rectangle:

  def __init__(self, width, height, x, y) -> None:
    self.width = width
    self.height = height

    # x and y represent the co-ordinates of the center of the rectangle
    self.x = x
    self.y = y 

  def area(self):
    return self.width * self.height
  
  def distance_to_point(self, point_x, point_y):
    x_distance = point_x - self.x
    y_distance = point_y - self.y

    distance = (x_distance ** 2 + y_distance ** 2) ** (1/ 2)  
    return distance

rectangle = Rectangle(108, 75, 70, 30)
print(rectangle.area())
print(rectangle.distance_to_point(190, 80))