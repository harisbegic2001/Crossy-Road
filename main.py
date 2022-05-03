from turtle import Screen
from player import Player
from board import Board
from cars import Car
import time
#Creation of screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("TURTLE CROSSING")
screen.tracer()


#Create a player
kornjaca = Player()

#Game Control
screen.listen()
screen.onkeypress(kornjaca.move_forward, "w")

#Level Board
level = Board()
level.display_level()

lista =[]
#Car

for i in range(10):
    car = Car()
    lista.append(car)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    for auto in lista:
        auto.move_left()
        if auto.xcor() < -280:
            auto.setx(280)
        if kornjaca.ycor() > 280:
            level.increase_level()
            kornjaca.sety(-280)
            for auto in lista:
                auto.increase_speed()
                auto.shuffle_location()
        if kornjaca.distance(auto) < 20:
            level.game_over()
            game_is_on = False





























screen.exitonclick()
