#Chichirita Mandala Art
import turtle
turtle.speed(0)
turtle.bgcolor("#DBDBDB")
turtle.title("Chichirita Mandala Art")

def position(x, y):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()

def octagon(x):
    for i in range(8):
        turtle.forward(x)
        turtle.left(45)

def box(x, c):
    turtle.fillcolor(c)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(x)
        turtle.left(90)
    turtle.end_fill()

def box2(x, c):
    turtle.fillcolor(c)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(x)
        turtle.right(45)
        turtle.forward(x)
        turtle.right(135)
    turtle.end_fill()

def petal(x, y):
    turtle.circle(x, y)
    turtle.left(180 - y)
    turtle.circle(x, y)
    turtle.left(90 - y)

def flower(x, y, c):
    turtle.fillcolor(c)
    turtle.begin_fill()
    for i in range(4):
        petal(x, y)
        turtle.right(180)
    turtle.end_fill()

def star(x, c):
    turtle.fillcolor(c)
    turtle.begin_fill()
    for i in range(8):
        turtle.left(45)
        turtle.forward(x)
        turtle.right(45)
        turtle.forward(x)
        turtle.left(45)
    turtle.end_fill()

position(0, -170.82337649)
turtle.pensize(2)
turtle.fillcolor("#2F4F75")
turtle.begin_fill()
turtle.circle(173.82337649)
turtle.end_fill()

position(0, -170.82337649)
star(72, "#950F7D")

position(0, -140)
turtle.fillcolor("#9F45B0")
turtle.begin_fill()
turtle.left(22.5)
octagon(110)
turtle.end_fill()
turtle.right(22.5)

position(0, -120)
turtle.fillcolor("#9A9CC2")
turtle.begin_fill()
turtle.circle(120)
turtle.end_fill()

position(0, -120.71067812)
star(50, "#D5E9F4")

turtle.pensize(1)
position(0,0)
for i in range(8):
    turtle.left(45)
    octagon(50)

position(-50, -120.71067812)
turtle.color("#9F45B0")
turtle.pensize(2)
octagon(100)

turtle.color("black")
turtle.pensize(3)
position(0, -140)
turtle.left(22.5)
octagon(110)
turtle.end_fill()
turtle.right(22.5)

turtle.pensize(1)
turtle.left(45)
position(0, -120.71067812)
box(50, "#99BDDF")
position(0, 50)
box(50, "#99BDDF")
position(-85.35533906, -35.35533906)
box(50, "#99BDDF")
position(85.35533906, -35.35533906)
box(50, "#99BDDF")
turtle.right(45)
position(-85.35533906, 35.35533906)
box(50, "#F0E9F9")
position(35.35533906, 35.35533906)
box(50, "#F0E9F9")
position(-85.35533906, -85.35533906)
box(50, "#F0E9F9")
position(35.35533906, -85.35533906)
box(50, "#F0E9F9")

position(0,0)
for i in range(4):
    box2(50, "#CBBBD6")
    turtle.right(90)
turtle.left(90)

turtle.right(33.5)
flower(30, 110, "#D3DFED")
turtle.right(45)
flower(30, 110, "#D3DFED")
turtle.right(11.5)
turtle.right(40)
flower(30, 80, "#E2BCB7")
turtle.left(45)
flower(30, 80, "#E2BCB7")

turtle.hideturtle()
turtle.done()