from tkinter import XView
import matplotlib.pyplot as plt
import sys

class Paint:
    def __init__(self, width, height):
        self.canvas = []
        for line in range(height):
            line_data = list()
            for col in range(width):
                line_data.append([255, 255, 255])
            self.canvas.append(line_data)

    def set_pixel(self, x, y, r=0, g=0, b=0):
        if y >= len(self.canvas):
            raise Exception("Y too high")
        if x >= len(self.canvas[y]):
            raise Exception("X too high")
        if x < 0 or y < 0:
            raise Exception("Coordinate < 0")

        self.canvas[y][x] = [r, g, b]

    def show(self):
        plt.imshow(self.canvas)
        plt.gca().invert_yaxis()
        plt.show()
        sys.exit(0)

class Point:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def area(self):
        return 0.0

    @property
    def perimeter(self):
        return 0.0

    @property
    def stretch(self, width_factor, height_factor):
        return Point(self.x, self.y)

    def is_inside(self, x, y):
        return (self.x == x) and (self.y == y)

    def draw(self, paint):
        paint.set_pixel(self.x, self.y)

class Rectangle(Point):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return self.height * 2 + self.width * 2

    @property

    def stretch(self, width_factor, height_factor):
        new_width = self.width * width_factor
        new_height = self.height * height_factor
        return Rectangle(self.x, self.y, new_width, new_height)

    def is_inside(self, x, y):
        return (self.x == x) and (self.y == y)

    def draw(self, paint):
        paint.set_pixel(self.x, self.y, self.width, self.height)

class Carre(Rectangle):
    def __init__(self, x, y, size):
        # A square is a rectangle with equal width and height
        Rectangle.__init__(self, x, y, size, size)

    @property
    def area(self):
        return self.width ** 2

    @property
    def perimeter(self):
        return 4 * self.width
class Triangle(Point):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self._width = width
        self._height = height

    @property
    def area(self):
        # Aire d'un triangle : (base * hauteur) / 2
        return (self._width * self._height) / 2

    @property
    def perimeter(self):
        hypotenuse = (self._width**2 + self._height**2) ** 0.5
        return self._width + self._height + hypotenuse

    def stretch(self, width_factor, height_factor):
        new_width = self._width * width_factor
        new_height = self._height * height_factor
        return Triangle(self.x, self.y, new_width, new_height)

    def is_inside(self, x, y):
        if x < self.x or y < self.y:
            return False
        return (y - self.y) <= (-self._height / self._width) * (x - self.x) + self._height

    def draw(self, paint):
        for i in range(self._width):
            for j in range(int(self._height * (i / self._width)) + 1):
                paint.set_pixel(self.x + i, self.y + j, 0, 0, 0)
    class Triangle Isocele:
        
paint = Paint(100, 100)
### Geometric objects here
pt = Rectangle(15, 25, 20,10)
pt.draw(paint)
paint.show()
# Create a Paint object with dimensions 100x100
paint = Paint(100, 100)

# Create a rectangle at position (10, 10) with width 30 and height 15
rectangle = Rectangle(10, 10, 30, 15)
rectangle.draw(paint)

# Create a square at position (50, 50) with size 20
square = Carre(50, 50, 20)
square.draw(paint)

# Display the drawing
paint.show()
###
# TODO        Rectangle
# TODO        Cercle
# TODO        Carré
# TODO        Ellipse
# TODO        Triangle
# TODO        Parallèlogramme
