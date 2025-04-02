from turtle import *

speed(0)
bgcolor("black")

penup()
goto(-350,100)
pendown()
fillcolor("blue")
begin_fill()#The begin_fill() function in the Turtle module is used to start filling a shape with the specified fill color. When you call begin_fill(), any shape drawn afterward will be filled with the color set by fillcolor() once you call end_fill().
for i in range(3):
    forward(300)
    left(120)
end_fill()

# multicolor
penup()
goto(-10,100)
pendown()
for i in ["pink","red","blue"]:
    color(i)
    forward(300)
    left(120)

hideturtle()
done()
