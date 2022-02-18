from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = 7
        if random.randint(1, 7) == random_number:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(350, random_y)
            self.cars.append(new_car)

    def move_car(self, level):
        for car in self.cars:
            car.forward(self.car_speed)

    def increase_car_speead(self):
        self.car_speed += MOVE_INCREMENT





