import time
from turtle import Screen
from snake import Snake
import food
from scoreboard import Score
a = Screen()
a.setup(width=1.0, height=1.0)
a.bgcolor("black")
a.title("a game by abhi")
a.screensize(600, 600)
a.listen()
x = Snake()
a.onkey(x.up, "Up")
a.onkey(x.down, "Down")
a.onkey(x.left, "Left")
a.onkey(x.right, "Right")
f = food.Food()
k = Score()

while True:
    time.sleep(0.2)
    if x.head.distance(f.me[0]) < 15:
        k.update(len(x.turtles)-2)
        f.refresh()
        x.adds()
    for hm in x.turtles[1:]:
        if hm.distance(x.head) < 10:
            k.game_over()
            time.sleep(5)
            quit()
    a.update()
    x.move(10)
    if x.head.xcor() >= 290 or x.head.xcor() <= -290 or x.head.ycor() >= 220 or x.head.ycor() <= -290:
        k.game_over()
        time.sleep(5)
        quit()
