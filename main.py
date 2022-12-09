from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
segment = Turtle()
segment.color("white")

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
segment.hideturtle()
segment.penup()
segment.goto(0, -300)


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(paddle_r.go_up, "Up")
screen.onkeypress(paddle_r.go_down, "Down")
screen.onkeypress(paddle_l.go_up, "w")
screen.onkeypress(paddle_l.go_down, "s")

segment.left(90)

for _ in range(100):
    segment.forward(10)
    segment.penup()
    segment.forward(10)
    segment.pendown()

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with Paddle 
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when paddle R misses
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.point_R()

    # Detect when paddle L misses
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.point_L()


screen.exitonclick()