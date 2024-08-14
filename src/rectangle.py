from src.point import Point


class Rectangle:
    def __init__(self, upper_right: Point, lower_left: Point):
        self.upper_right = upper_right
        self.lower_left = lower_left

    def check_point_inside(self, point_to_check: Point) -> bool:
        if self.upper_right.x > point_to_check.x > self.lower_left.x \
                and self.upper_right.y > point_to_check.y > self.lower_left.y:
            return True

        return False

    def get_area(self):
        x = abs(self.upper_right.x - self.lower_left.x)
        y = abs(self.upper_right.y - self.lower_left.y)
        area = x * y
        return area
