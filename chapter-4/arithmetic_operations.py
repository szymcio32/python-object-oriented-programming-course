# print(5 + 5)
# print(int.__add__(5, 5))
#
## 5 + 5 == int.__add__(5, 5)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'x, y: {self.x}, {self.y}'

    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            x = self.x - other.x
            y = self.y - other.y
            return Point(x, y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Point):
            x = self.x * other.x
            y = self.y * other.y
            return Point(x, y)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Point):
            x = self.x / other.x
            y = self.y / other.y
            return Point(x, y)
        return NotImplemented


point_1 = Point(5, 5)
point_2 = Point(5, 5)
point_3 = point_1 + point_2
point_4 = point_1 - point_2
point_5 = point_1 * point_2
point_6 = point_1 / point_2
print(f'__add__\t {point_3}')
print(f'__sub__\t {point_4}')
print(f'__mul__\t {point_5}')
print(f'__truediv__\t {point_6}')

# point_7 = point_1 + '5, 5'