#
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # @staticmethod: class method that acts like an additional arm
    # def area(width, height):
    # return width * height


w = int(input())
h = int(input())
x = Shape(w, h)
print(x.area())


try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)

x = 0
try:
  x+=1
  raise ValueError
except NameError:
  x+=1
except ValueError:
  x+=1
else:
  x+=1
finally:
  x+=1
  print(x)