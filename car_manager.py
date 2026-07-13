from turtle import Turtle, Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10




class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []


    def generate_car(self):
        tillu = Turtle(shape="square")
        tillu.color(random.choice(COLORS))
        tillu.shapesize(stretch_wid=1, stretch_len=2)
        tillu.penup()
        tillu.goto(random.randint(300,600) ,  random.randint(-250,250))
        tillu.setheading(180)
        self.cars.append(tillu)

    def move(self):
        for i in self.cars:
            i.forward(STARTING_MOVE_DISTANCE)

    def next_level(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
