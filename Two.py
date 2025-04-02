import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)  
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(180):  
    pen.color(colors[i % 7]) 
    pen.forward(i * 3 / math.pi)  
    pen.left(59)  
    pen.forward(i * 3 / math.pi)
    pen.left(59)
screen.exitonclick()

