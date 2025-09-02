class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.isfilled = is_filled

    def describe(self):
        print (f'It is {self.color} and {'Filled ' if {self.isfilled} else 'Not filled'}')


class Circle (Shape):
    def __init__(self, radius, color, is_filled):
        super ().__init__ (color, is_filled)
        self.radius = radius

    def describe(self):
        print(f' It is a circle with an area of {3.14 * self.radius * self.radius}')
        super().describe()


class Square (Shape):
    def __init__(self, color, is_filled, width):
        super ().__init__ (color, is_filled)
        self.width = width


circle = Circle (5, 'Red', True)

print (circle.color)
circle.describe()
