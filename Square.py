from turtle import *

bgcolor("black")# back ground colour
speed(1)
penup()
goto(-150,-100)
pendown()
fillcolor("red")
begin_fill()

for i in range(4):
    forward(300)
    left(90)
end_fill()
hideturtle()
done()
