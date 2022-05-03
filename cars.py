from turtle import Turtle
import random as r
colors = ["red", "green", "blue", "yellow", "brown"]
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.brzina = 10
        self.color(colors[r.randint(0,len(colors)-1)])
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.speed("fastest")
        self.goto(x=280, y=r.randint(-270, 270))
        self.setheading(-180)

    def move_left(self):
        self.forward(self.brzina)

    def increase_speed(self):
        self.brzina += 5

    def shuffle_location(self):
        self.setx(r.randint(-270,270))