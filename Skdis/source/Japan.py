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

turtle.reset()
turtle.speed(0)
#turtle.delay(0)
height = 100
width = 100 * 3 / 2
rect(-120, 160, 'gray', 120, -160)
rect(-width/2, height/2, 'white', width/2, -height/2)

r = height*0.6/2
turtle.penup()
turtle.home()
turtle.forward(r)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(90)
turtle.color('red', 'red')
turtle.circle(r)
turtle.end_fill()
