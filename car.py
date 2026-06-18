from turtle import Turtle
import random

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        # self.color("blue")
        self.speed("fastest")
        self.setheading(180)
        x= random.randint(-280, 280)
        y= random.randint(-260, 280)
        self.goto(x, y)
    
    def moveCar(self, rate):
        self.forward(rate)