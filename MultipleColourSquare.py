from turtle import *
bgcolor("black")
pensize(3)
penup()
goto(-150,-100)
pendown()
for i in ["pink","red","blue","purple"]:
    color(i)
    forward(300)
    left(90)
hideturtle()
done()