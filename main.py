import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
game_is_on = True
screen.listen()
screen.onkey(player.move, "space")
cars = []
round = 1
cycle = 0
while game_is_on:
    scoreboard.round_num(round)
    time.sleep(0.1)
    cycle += 1
    screen.update()
    for item in cars:
        item.forward(10)
    if cycle % (5-round) == 0:
        cars.append(CarManager())
        iteration = 0
        for _ in range(len(cars)):
            _ -= iteration
            if cars[_].xcor() < -300:
                cars[_].ht()
                cars[_].clear()
                del cars[_]
                iteration += 1
    if player.ycor() > 270:
        if round < 5:
            round += 1
        player.goto(0,  -280)
    for car in cars:
        if car.ycor() + 20 > player.ycor() > car.ycor() - 20:
            print("HITTTT Y")
            if car.xcor() + 32 > player.xcor() > car.xcor() - 32:
                print("HITT X")
                player.goto(0, -280)



