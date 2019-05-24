import uturtle

turtle = uturtle.Turtle()

def rect(x, y, color, x2, y2):
    width = abs(x2 - x)
    height = abs(y2 - y)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor(color)
    # turtle.color(color, color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()

def germany():
    rect(-75,50,'black',75,16)
    rect(-75,16,'red',75,-16)
    rect(-75,-17,'gold',75,-50)

turtle.reset()
turtle.speed(0)
#turtle.delay(0)
germany()
