import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_player = Player()

screen.listen()
screen.onkey(game_player.go_up, "Up")
car_manager = CarManager()
score = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(game_player) < 20:
            score.game_over()
            game_is_on = False

    # next Leve
    if game_player.is_at_finish_line():
        game_player.go_to_start()
        car_manager.level_up()
        score.update()

screen.exitonclick()
