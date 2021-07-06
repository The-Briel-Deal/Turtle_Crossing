from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

        self.goto(-200, 250)
    def round_num(self, round):
        self.clear()
        self.write(f"Round: {round}", move=False, align="center", font=FONT)
