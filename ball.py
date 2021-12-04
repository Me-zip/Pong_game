'''
Created on Oct 23, 2021

@author: user
'''
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.shapesize(1)
        self.x_move=10
        self.y_move=10
        
    
    def move(self):
        y=self.ycor()+self.y_move
        x=self.xcor()+self.x_move
        self.penup()
        self.goto(x,y)
    
    def bounce_y(self):
        self.y_move *=-1
        
    def bounce_x(self):
        self.x_move *=-1
    
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()