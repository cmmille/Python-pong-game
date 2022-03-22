import time
from turtle import Screen
from setup import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WINNING_SCORE = 5

# Game table (screen)
table = Screen()
table.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
table.bgcolor("black")
table.listen()
table.tracer(False)

# Left paddle
left_paddle = Paddle()
left_paddle.set_left()

# Right paddle
right_paddle = Paddle()
right_paddle.set_right()

# Ball
ball = Ball()
ball.new_ball()

# Scoreboards
left_score = Scoreboard()
left_score.set_left()
right_score = Scoreboard()
right_score.set_right()

game_over = False
while not game_over:
    time.sleep(0.0025)
    table.update()

    table.onkey(key="w", fun=left_paddle.up)
    table.onkey(key="s", fun=left_paddle.down)
    table.onkey(key="Up", fun=right_paddle.up)
    table.onkey(key="Down", fun=right_paddle.down)

    left_paddle.hit_ball(ball)
    right_paddle.hit_ball(ball)

    # Ball hit:
    # Right side
    if ball.xcor() > SCREEN_WIDTH / 2:
        ball.new_ball()
        ball.collide_paddle()
        left_score.increase_score()
    # Left side
    elif ball.xcor() < -SCREEN_WIDTH / 2:
        ball.new_ball()
        ball.collide_paddle()
        right_score.increase_score()
    # Top side
    elif ball.ycor() >= SCREEN_HEIGHT / 2 - 20:
        ball.bounce()
    # Bottom side
    elif ball.ycor() <= -SCREEN_HEIGHT / 2 +20:
        ball.bounce()

    ball.move()

    if left_score.score >= WINNING_SCORE:
        left_score.game_over()
        game_over = True
    elif right_score.score >= WINNING_SCORE:
        right_score.game_over()
        game_over = True

table.exitonclick()
