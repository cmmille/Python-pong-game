from turtle import Turtle
from setup import *

STEP = 30

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4, 1)
        self.penup()

    def set_left(self):
        LEFT_POS = SCREEN_WIDTH / -2 + 40
        self.setx(LEFT_POS)

    def set_right(self):
        RIGHT_POS = SCREEN_WIDTH / 2 - 40
        self.setx(RIGHT_POS)

    def up(self):
        MAX_Y = SCREEN_HEIGHT / 2 - 80
        if self.ycor() <= MAX_Y:
            self.sety(self.ycor() + STEP)

    def down(self):
        MIN_Y = SCREEN_HEIGHT / -2 + 80
        if self.ycor() >= MIN_Y:
            self.sety(self.ycor() - STEP)

    def hit_ball(self, ball):
        if ball.distance(self) < 40 and ball.xcor() > SCREEN_WIDTH/2 -60:
            ball.collide_paddle()
        elif ball.distance(self) < 40 and ball.xcor() < -SCREEN_WIDTH/2 +60:
            ball.collide_paddle()
