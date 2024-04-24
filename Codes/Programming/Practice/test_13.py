import math

class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

name1 = input("Введите имя первой точки: ").strip()
x1, y1 = map(float, input("Введите координаты первой точки через пробел: ").split())
name2 = input("Введите имя второй точки: ").strip()
x2, y2 = map(float, input("Введите координаты второй точки через пробел: ").split())
A = Point(name1, x1, y1)
B = Point(name2, x2, y2)
print(A)
print(B)
print(f"{name1} {name2} = {A.distance(B)}")
