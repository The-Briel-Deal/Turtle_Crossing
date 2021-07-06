import turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLORS[random.randint(0, 5)])
        self.goto(500, random.randint(-200, 250))
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2.3)


