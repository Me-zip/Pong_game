'''
Created on Oct 22, 2021

@author: user
'''
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import scoreboard

import time

screen=Screen()

screen.bgcolor("black")
screen.setup(width=800,height=600) 
screen.title("Pong Game")
screen.tracer(0)

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
scoreboard=scoreboard()

screen.listen()
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

is_game_on=True
while(is_game_on):
    time.sleep(0.1)
    screen.update()
    ball.move()
    #Detect collision with upper wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()
    
    #detect collision with paddle
    if ball.distance(r_paddle) <50 and ball.xcor() >340 or ball.distance(l_paddle)<50 and ball.xcor() <-340:
        ball.bounce_x()
    
    #Detect collision with side walcl
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()