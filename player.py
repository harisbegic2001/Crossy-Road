from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.sety(-280)
        self.setheading(90)



    def move_forward(self):
        self.forward(5)
