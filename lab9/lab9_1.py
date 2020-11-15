import turtle
from random import randint

start = "2222220"
axmTemp = ""

stride_length = 10
angle = 15
position = []

turtle.hideturtle()
turtle.penup()
turtle.setpos(0, -300)
turtle.left(90)
turtle.pendown()
turtle.tracer(0)
turtle.pensize(2)

regulations = {"0": "1[-20]+20",
               "1": "12"}

for k in range(11):
    for i in start:
        if i in regulations:
            axmTemp += regulations[i]
        else:
            axmTemp += i
    start = axmTemp
    axmTemp = ""

for i in start:
    if i == "1":
        if randint(0, 10) >= 5:
            turtle.forward(stride_length)
    elif i == "+":
        turtle.right(angle - randint(-14, 14))
    elif i == "2":
        if randint(0, 10) >= 5:
            turtle.forward(stride_length)
    elif i == "-":
        turtle.left(angle - randint(-5, 5))
    elif i == "0":
        r_color = randint(1, 6)
        if r_color == 1:
            turtle.pencolor('#006400')
        elif r_color == 2:
            turtle.pencolor('#228B22')
        elif r_color == 3:
            turtle.pencolor('#00FF7F')
        elif r_color == 4:
            turtle.pencolor('#DC143C')
        elif r_color == 5:
            turtle.pencolor('#8B0000')
        elif r_color == 6:
            turtle.pencolor('#FFFFE0')
        turtle.forward(stride_length)
        turtle.pencolor('#000000')
    elif i == "[":
        position.append(turtle.xcor())
        position.append(turtle.ycor())
        position.append(turtle.heading())
    elif i == "]":
        turtle.penup()
        turtle.setheading(position.pop())
        turtle.sety(position.pop())
        turtle.setx(position.pop())
        turtle.pendown()

turtle.update()
turtle.mainloop()
