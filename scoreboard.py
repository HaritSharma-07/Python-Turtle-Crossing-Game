from turtle import Turtle
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.c_level = 1
        self.level_status()


    def level_status(self):
        self.clear()
        self.goto(x=-230, y=260)
        self.write(f"level : {self.c_level}", align="center", font=FONT)


    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(f"FINAL SCORE : {self.c_level}\n   GAME OVER", align="center", font=FONT)



    def level_increment(self):
        self.c_level += 1
        self.level_status()