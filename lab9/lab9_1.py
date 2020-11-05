import turtle

start = "a"
axmTemp = ""

stride_length = 16

turtle.hideturtle()
turtle.penup()
turtle.setpos(-250, 170)
turtle.pendown()
turtle.tracer(0)
turtle.pensize(2)

regulations = {"a": "b---a---b",
               "b": "a++b++a"}

for k in range(11):
    for i in start:
        if i in regulations:
            axmTemp += regulations[i]
        else:
            axmTemp += i
    start = axmTemp
    axmTemp = ""

for i in start:
    if i == "+":
        turtle.right(60)
    elif i == "-":
        turtle.left(60)
    else:
        turtle.forward(stride_length)

turtle.update()
turtle.mainloop()
