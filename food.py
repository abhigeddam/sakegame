from turtle import Turtle
from random import randint


class Food:
    def __init__(self):
        self.pos = []
        self.me = []
        self.create()

    def create(self):
        print(self.pos)
        f = Turtle()
        self.me.append(f)
        f.shape('square')
        f.speed("fast")
        f.shapesize(.3)
        self.refresh()

    def refresh(self):
        x = randint(-270, 270)
        y = randint(-270, 250)
        self.me[0].penup()
        self.me[0].color("black")
        self.me[0].goto(x, y)
        self.me[0].color("pink")




