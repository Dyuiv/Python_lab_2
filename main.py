import math

class Shape:
    def __init__(self, n_angles, angles=None, sides=None):
        if (n_angles < 0 or (angles and len(angles) != n_angles) or (sides and len(sides) != n_angles)):
            raise ValueError("Неверное количество углов или сторон")
        if (angles and not all(0 < angle < 360 for angle in angles)):
            raise ValueError("Угол должен быть положителен и меньше 360 градусов")
        if (sides and not all(side > 0 for side in sides)):
            raise ValueError("Длины сторон должны быть положительными")
        self.n_angles = n_angles
        self.angles = angles if angles else []
        self.sides = sides if sides else []

    def get_perimeter(self):
        if not self.sides:
            return 0
        return sum(self.sides)
    def get_info(self):
        return {
            "angles": self.angles,
            "sides": self.sides,
            "perimeter": self.get_perimeter()
        }

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        super().__init__(0)
        self.radius = radius
        self.name = "Circle"
    def get_sq(self):
        return (math.pi * self.radius ** 2)

    def get_info(self):
        info = super().get_info()
        info.update({"name": self.name, "radius": self.radius, "area": self.get_sq()})
        return info

class Triangle(Shape):
    def __init__(self, angles, sides):
        if (len(angles) != 3 or len(sides) != 3):
            raise ValueError("У треугольника должно быть 3 угла и 3 стороны")
        if (sum(angles) != 180):
            raise ValueError("Сумма углов треугольника должна быть 180 градусов")
        super().__init__(3, angles, sides)
        self.name = "Triangle"

    def get_sq(self):
        try:
            a, b, c = self.sides
            p = (a + b + c) / 2
            heron_area = math.sqrt(p * (p - a) * (p - b) * (p - c))
            h = (2 / a) * heron_area
            def_area = 0.5 * a * h
            angle_radians = math.radians(self.angles[0])
            sine_area = 0.5 * a * b * math.sin(angle_radians)
            return def_area
        except:
            return "Невозможно вычислить площадь"

    def get_info(self):
        info = super().get_info()
        info.update({"name": self.name, "area": self.get_sq()})
        return info

class Quadrangle(Shape):
    def __init__(self, angles, sides):
        if (len(angles) != 4 or len(sides) != 4):
            raise ValueError("У четырехугольника должно быть 4 угла и 4 стороны")

        if (sum(angles)!= 360):
            missing_angle = 360 - sum(angles) - 1
            angles = [missing_angle if angle == -1 else angle for angle in angles]
        super().__init__(4, angles, sides)
        self.name = "Quadrangle"
    def is_rectangle(self):
        return all(angle == 90 for angle in self.angles)
    def is_parallelogram(self):
        return self.angles[0] == self.angles[2] and self.angles[1] == self.angles[3]
    def is_trapezoid(self):
        return self.sides[0] != self.sides[2] and self.sides[1] != self.sides[3]
    def get_sq(self):
        try:
            if self.is_rectangle():
                return (self.sides[0] * self.sides[1])
            elif self.is_parallelogram():
                base, side, angle = self.sides[0], self.sides[1], self.angles[0]
                return (base * side * math.sin(math.radians(angle)))
            elif self.is_trapezoid():
                a, b, c, d = self.sides
                h = math.sqrt(c ** 2 - ((b - a) ** 2 / 4))
                return (0.5 * (a + b) * h)
            else:
                raise ValueError("Неизвестный тип четырехугольника")
        except:
            return "Невозможно вычислить площадь"

    def get_info(self):
        info = super().get_info()
        info.update({"name": self.name, "area": self.get_sq()})
        return info

class Nangle(Shape):
    def __init__(self, n_angles, angles=None, sides=None):
        if (not angles and not sides):
            raise ValueError("n-угольник должен иметь хотя бы углы или стороны")
        super().__init__(n_angles, angles, sides)
        self.name = f"{n_angles}-angle"

    def get_sq(self):
        return "Подсчёт площади n-угольника не реализован"

    def get_info(self):
        info = super().get_info()
        info.update({"name": self.name, "area": self.get_sq()})
        return info

try:

    circle = Circle(radius=5)
    print(circle.get_info())

    triangle = Triangle(angles=[60, 60, 60], sides=[3, 4, 5])
    print(triangle.get_info())

    quadrangle = Quadrangle(angles=[90, 90, 90, -1], sides=[10, 10, 10, 10])
    print(quadrangle.get_info())

    nangle = Nangle(7, angles=None, sides=[10,10,10,10,10,10,10])
    print(nangle.get_info())
except Exception as e:
    print(e)
