import time
from turtle import Screen, Turtle
from car import Car
import random


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
game_is_on = True


turtle = Turtle("turtle")
turtle.penup()
turtle.color("black")
turtle.setheading(90)
turtle.goto(0, -270)
rate = 10
score = 0
# turtle.speed(10)
cars = Car()
def MoveUp():
    turtle.forward(10)

screen.listen()
screen.onkey(MoveUp, "Up")


while game_is_on:
    time.sleep(0.1)
    cars.createCar()
    cars.moveCar(rate)
    screen.update()
    game_is_on = cars.checkTurtle(turtle, score)
    if(turtle.ycor()>300):
        rate+=2
        turtle.goto(0, -270)
        score +=1

screen.exitonclick()