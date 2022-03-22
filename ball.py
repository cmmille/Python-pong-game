from turtle import Turtle
from setup import *

STEP = SCREEN_WIDTH/300

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(0.5)
        self.step = STEP
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.xcor() + self.x_move*self.step
        new_y = self.ycor() + self.y_move*self.step
        self.goto(new_x, new_y)

    def new_ball(self):
        self.step = STEP
        self.setpos(0,0)

    def collide_paddle(self):
        self.x_move *= -1
        self.step+=0.25

    def bounce(self):
        self.y_move *= -1
