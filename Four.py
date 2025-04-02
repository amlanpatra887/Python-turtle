import turtle
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)  
pen.pensize(1)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(180):
    pen.color(colors[i % len(colors)]) 
    pen.circle(100, 90) 
    pen.left(98)  

screen.exitonclick()
