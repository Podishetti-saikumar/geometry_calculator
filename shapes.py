import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        if isinstance(other, Point):
            return math.hypot(self.x - other.x, self.y - other.y)
        return other.distance(self)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def length(self):
        return self.start.distance(self.end)

    def distance(self, other):
        if isinstance(other, Point):
            x0, y0 = other.x, other.y
            x1, y1 = self.start.x, self.start.y
            x2, y2 = self.end.x, self.end.y
            numerator = abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1))
            denominator = self.length()
            return numerator / denominator if denominator != 0 else 0.0
        return min(self.start.distance(other), self.end.distance(other))

    def __repr__(self):
        return f"Line({self.start}, {self.end})"

class Circle:
    def __init__(self, center: Point, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def distance(self, other):
        if isinstance(other, Point):
            dist = self.center.distance(other) - self.radius
            return max(0.0, dist)
        elif isinstance(other, Circle):
            dist = self.center.distance(other.center) - self.radius - other.radius
            return max(0.0, dist)
        return max(0.0, other.distance(self.center) - self.radius)

    def __repr__(self):
        return f"Circle({self.center}, {self.radius})"

class Rectangle:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.min_x = min(p1.x, p2.x)
        self.max_x = max(p1.x, p2.x)
        self.min_y = min(p1.y, p2.y)
        self.max_y = max(p1.y, p2.y)

    def area(self):
        return (self.max_x - self.min_x) * (self.max_y - self.min_y)

    def perimeter(self):
        return 2 * ((self.max_x - self.min_x) + (self.max_y - self.min_y))

    def distance(self, other):
        if isinstance(other, Point):
            if (self.min_x <= other.x <= self.max_x and
                self.min_y <= other.y <= self.max_y):
                return 0.0
            dx = max(self.min_x - other.x, other.x - self.max_x, 0.0)
            dy = max(self.min_y - other.y, other.y - self.max_y, 0.0)
            return math.hypot(dx, dy)
        corners = [Point(self.min_x, self.min_y), Point(self.min_x, self.max_y),
                   Point(self.max_x, self.max_y), Point(self.max_x, self.min_y)]
        return min(corner.distance(other) for corner in corners)

    def __repr__(self):
        return f"Rectangle({self.p1}, {self.p2})"