import random

from src.point import Point
from src.rectangle import Rectangle


class Game:
    def __init__(self):
        self.rec = None

    def game_loop(self):
        playing = True
        while playing:
            self.initiate_the_game()
            print(f"The rectangle is defined by points {self.rec.upper_right.print()}" +
                  f" and {self.rec.lower_left.print()}")
            point = input("Please guess a point that is in the rectangle: [in int format (x, y)]\n")
            point = point.split(sep=',')
            interpreted_ans = [int(''.join(filter(str.isdigit, cor))) for cor in point]
            answer_point = Point(interpreted_ans[0], interpreted_ans[1])
            if self.rec.check_point_inside(answer_point):
                print("Nice! You guessed it right")
            else:
                print("Oh no! The point you provided is not in the rectangle")

            area = int(input("Please calculate the area of the rectangle: (please provide a number only)\n"))
            correct_area = self.rec.get_area()

            if area != correct_area:
                print("Oh no! You miscalculated the area!")
            else:
                print("Great! You get it right!")

            quit_or_not = input("Wanna continue? (enter y or n)\n")
            if quit_or_not == 'n':
                playing = False

    def initiate_the_game(self):
        upper_right = Point(random.randint(0, 10), random.randint(0, 10))
        lower_left = Point(random.randint(-10, 0), random.randint(-10, 0))
        self.rec = Rectangle(upper_right, lower_left)
