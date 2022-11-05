from turtle import Screen,Turtle
import time
Start_position = [[0,0],[-10,0],[-20,0]]


class Snake():
    def __init__(self):
        self.turtles = []
        self.create_snakes()
        self.head = self.turtles[0]

    def create_snakes(self):
        for hm in Start_position:
            Screen().update()
            a = Turtle()
            a.penup()
            a.shape("circle")
            a.shapesize(.5)
            a.color("red")
            a.goto(hm[0],hm[1])
            self.turtles.append(a)

    def adds(self):
        Screen().update()
        a = Turtle()
        a.penup()
        a.shape("circle")
        a.shapesize(.5)
        self.turtles.append(a)
        a.goto(self.turtles[-2].xcor(),self.turtles[-2].ycor())
        a.color("red")

    def move(self,n):
        for hm in range(len(self.turtles)-1,0,-1):
            x1 = self.turtles[hm-1].xcor()
            y1 = self.turtles[hm-1].ycor()
            self.turtles[hm].goto(x1,y1)
        self.head.forward(n)

    def up(self):
        if self.head.heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.turtles[0].setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.turtles[0].setheading(0)



