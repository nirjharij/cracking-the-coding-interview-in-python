class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.slope = (end.y - start.y) / (end.x - start.x)
        self.intercept = end.y - self.slope * end.x


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Intersection:
    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2

    def find_intersection(self):
        if self.line1.slope == self.line2.slope:
            if self.line1.intercept == self.line2.intercept and \
                    self.is_between(self.line1.start, self.line2.start, self.line1.end):
                return self.line2.start2
            return None
        x = (self.line2.intercept - self.line1.intercept) / (self.line1.slope - self.line2.slope)
        y = x * self.line1.slope + self.line1.intercept
        intersection_point = Point(x, y)

        if self.is_between(self.line1.start, intersection_point, self.line1.end) and \
                self.is_between(self.line2.start, intersection_point, self.line2.end):
            return intersection_point
        else:
            return None

    def is_between(self, start, middle, end):
        if start.x > end.x and start.y > end.y:
            return middle.x >= end.x and middle.y >= end.y and middle.x <= start.x and middle.y <= start.y
        else:
            return middle.x <= end.x and middle.y <= end.y and middle.x >= start.x and middle.y >= start.y

