from turtle import Turtle

FONT = ('Arial', '60', 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.updateScore()

    def updateScore(self):
        self.goto(-100, 200)
        self.write(f"{self.score_l}", False, font=(FONT))
        self.goto(50, 200)
        self.write(f"{self.score_r}", False, font=(FONT))

    def point_R(self):
        self.score_r += 1
        self.clear()
        self.updateScore()
        print("Goal! Score for User Right")

    def point_L(self):
        self.score_l += 1
        self.clear()
        self.updateScore()
        print("Goal! Score for User Left")
