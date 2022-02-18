import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=600)
screen.listen()
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car(scoreboard.level)

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_car_speead()
        scoreboard.update_level()

scoreboard.game_over()
screen.exitonclick()
