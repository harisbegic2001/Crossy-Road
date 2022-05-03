from turtle import Turtle

class Board(Turtle):

    def __init__(self):
        super().__init__()

        self.speed("fastest")
        self.color("black")
        self.penup()
        self.goto(x=-230, y=250)
        self.level = 1
        self.hideturtle()

    def display_level(self):
        self.write(f"Current level:{self.level}", align="center", font=("Arial", 14, "normal"))


    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Current level:{self.level}", align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))