
from turtle import Turtle,Screen



class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)
    def up(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)
    
    def down(self):
        y=self.ycor()-20
        self.goto(self.xcor(),y)

