import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from project_day_23.player import FINISH_LINE_Y
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
player = Player()
count = 5
car_manager = CarManager()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(player.player_go_up, "Up")

game_is_on = True
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()

    if count % 5 == 0:
        car_manager.generate_car()

    scoreboard.level_status()

    car_manager.move()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.distance(x=0,y=280) < 15:
        player.player_go_down()
        car_manager.next_level()
        scoreboard.level_increment()


screen.exitonclick()