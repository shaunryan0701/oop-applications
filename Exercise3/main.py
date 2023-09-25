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
  

  def time_to_point(self, x, y, speed):
    time = self.distance_to_point(x, y) / speed
    return time
    
  def perimeter(self):
    return (self.width * 2) + (self.height * 2)

rectangle = Rectangle(3, 4, x=1, y=2)
print(rectangle.area())
print(rectangle.distance_to_point(190, 80))
print(rectangle.time_to_point(2, 3, 20))
print(rectangle.perimeter())