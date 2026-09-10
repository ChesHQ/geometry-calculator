import match

class Circle:
  def init (self, radius: float):
    if radius <= 0:
      raise ValueError("Радиус должен быть положительным")
    self.radius = radius
    
  def area(self) -> float:
    return math.pi * (self.radius ** 2)
