import time
from turtle import Screen, Turtle
from car import Car
import random


screen = Screen()
# screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
game_is_on = True


turtle = Turtle("turtle")
turtle.penup()
turtle.color("black")
turtle.setheading(90)
turtle.goto(0, -270)
# turtle.speed(10)
# car = Car()
color = ["blue", "black", "green", "yellow", "orange", "red", "grey", "purple"]
while game_is_on:
    color1 = color[random.randint(0,7)]
    car = Car(color1)
    car.moveCar(10)


def MoveUp():
    turtle.forward(10)

screen.listen()
screen.onkey(MoveUp, "Up")




screen.exitonclick()