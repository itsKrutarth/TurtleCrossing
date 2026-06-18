from turtle import Turtle
import random

class Car():

    def __init__(self):
        self.all_cars = []
        

    def createCar(self):
        randomChance1 = 3
        randomChance2 = 6
        randNum = random.randint(0, 10)
        if(randNum==randomChance1 or randNum==randomChance2):
            color = ["blue", "black", "green", "yellow", "orange", "red", "grey", "purple"]
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(color[random.randint(0,7)])
            car.speed("fastest")
            car.setheading(180)
            x= 280
            y= random.randint(-260, 260)
            car.goto(x, y)
            self.all_cars.append(car)
    
    def moveCar(self, rate):
        for car in self.all_cars:
            car.forward(rate)

    def checkTurtle(self, turtle, score):
        for car in self.all_cars:
            if (car.distance(turtle)<10):
                turtle2 = Turtle()
                turtle2.penup()
                turtle2.hideturtle()
                turtle2.color("black")
                turtle2.goto(0, 0)
                turtle2.write(f"GAME OVER :( Your Score: {score}", False, align="center", font=("Arial", 24, "normal"))
                return False
        return True