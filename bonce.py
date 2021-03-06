xmass = float(input("x mass: "))
if xmass > 50:
    xmass = float(input("input must be less than 50 "))

import turtle
import math

yvel = 0
xvel = -1
net = -xmass

wn = turtle.Screen()
wn.title("bonce")
wn.bgcolor("black")
wn.setup(width=1920, height=1080)
wn.tracer(0)

s = turtle.Turtle()
s.shape("square")
s.color("white")
s.shapesize(stretch_wid=3.2, stretch_len=50.35)
s.penup()
s.goto(-.5, 370)

h = turtle.Turtle()
h.shape("square")
h.color("black")
h.shapesize(stretch_wid=3, stretch_len=50.15)
h.penup()
h.goto(-.5, 370)

y = turtle.Turtle()
y.shape("square")
y.color("blue")
y.shapesize(stretch_wid=3, stretch_len=.1)
y.penup()
y.goto(-360, 370)

x = turtle.Turtle()
x.shape("square")
x.color("red")
x.shapesize(stretch_wid=3, stretch_len=.1)
x.penup()
x.goto(0, 370)

ly = turtle.Turtle()
ly.width(2)
ly.color("blue")
ly.penup()
ly.goto(-740, -400)
ly.pendown()
ly.left(90)
ly.forward(680)

lx = turtle.Turtle()
lx.width(2)
lx.color("red")
lx.penup()
lx.goto(-740, -400)
lx.pendown()
lx.forward(680*math.sqrt(xmass))

dot = turtle.Turtle()
dot.color("white")
dot.width(2)
dot.hideturtle()
dot.penup()
dot.goto((x.xcor()+500)*.68*math.sqrt(xmass)-740, (y.xcor()+502)*.68-400)
dot.pendown()

t = turtle.Turtle()
t.color("white")
t.width(2)
t.hideturtle()
t.penup()
t.goto(-740, -400)
t.pendown()
t.left(math.degrees(math.atan(math.sqrt(xmass**1)**-1)))
t.forward(math.sqrt(680**2+(680*math.sqrt(xmass))**2))

d = turtle.Turtle()
d.color("white")
d.width(2)
d.penup()
d.goto(680*math.sqrt(xmass)-740, -400)
d.pendown()
d.hideturtle()
d.left(90)
d.forward(680)

while True:
    wn.update()
    dot.setx((x.xcor()+500)*.68*math.sqrt(xmass)-740)
    dot.sety((y.xcor()+502)*.68-400)
    y.setx(y.xcor()+yvel)
    x.setx(x.xcor()+xvel)
    if y.xcor()-1 <= -503:
        yvel *= -1
        net += 2*yvel
    if x.xcor()+1 >= 501:
        xvel *= -1
        net += 2*xvel*xmass
    if x.xcor()-1 <= y.xcor()+1:
        xvel = (2*yvel+xvel*xmass-xvel)/(xmass+1)
        yvel = net-xvel*xmass,