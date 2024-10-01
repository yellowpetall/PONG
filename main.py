from turtle import Screen
from paddles import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
screen.tracer()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()

score = Score()

paddle1 = Paddle((350, 0))
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

paddle2 = Paddle((-350, 0))
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

ball = Ball()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.touched_paddle()

    if ball.xcor() > 400:
        ball.restart()
        score.l_point()
        paddle1.goto((350, 0))
        paddle2.goto((-350, 0))

    if ball.xcor() < -400:
        ball.restart()
        score.r_point()
        paddle1.goto((350, 0))
        paddle2.goto((-350, 0))

    if score.r_score == 5 or score.l_score == 5:
        ball.stop()
        score.game_over()
        game_on = False

screen.exitonclick()
