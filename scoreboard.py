from turtle import Turtle


class Score:
    def __init__(self):
        self.z = Turtle()
        self.B = Turtle()
        self.z.speed("fast")
        self.B.speed("fast")
        self.boarder()
        self.z.goto(-20, 230)
        self.z.pendown()
        self.z.color("green")
        self.z.write(f'score = 0', align="left", font=("arial", 12, "bold"))

    def update(self,n):
        self.z.clear()
        self.z.write(f'score = {n}', align="left", font=("arial", 12, "bold"))

    def game_over(self):
        self.z.penup()
        self.z.goto(0,0)
        self.z.pendown()
        self.z.write("GAME OVER", align="center", font=("arial", 22, "normal"))

    def boarder(self):
        self.B.color("yellow")
        self.B.penup()
        self.B.goto(-300,230)
        self.B.pendown()
        self.B.goto(300, 230)
        self.B.goto(300, -300)
        self.B.goto(-300,-300)
        self.B.goto(-300, 230)
        self.B.penup()



