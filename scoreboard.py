from turtle import Turtle
from setup import *
FONT = "courier"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.id = ""

        self.penup()
        self.color("white")
        self.hideturtle()
        self.sety(SCREEN_HEIGHT/2 - 60)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(self.score, True, align="center", font=(FONT, 32, "bold"))

    def increase_score(self):
        self.score += 1
        self.display_score()

    def set_left(self):
        self.id = "Left"
        self.setx(-SCREEN_WIDTH/4)
        self.display_score()

    def set_right(self):
        self.id = "Right"
        self.setx(SCREEN_WIDTH/4)
        self.display_score()

    def game_over(self):
        self.sety(0)
        self.color("red")
        message = f"{self.id} wins!"
        self.write(message, True, align="center", font=(FONT, 18, "bold"))

