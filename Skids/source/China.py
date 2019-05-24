import uturtle
turtle = uturtle.Turtle()

def draw_rect(x1, y1, color, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(color, color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_star(center_x, center_y, radius, color):
    turtle.penup()
    pt1=turtle.pos()
    turtle.circle(-radius, 72)
    pt2=turtle.pos()
    turtle.circle(-radius, 72)
    pt3=turtle.pos()
    turtle.circle(-radius, 72)
    pt4=turtle.pos()
    turtle.circle(-radius, 72)
    pt5=turtle.pos()

    turtle.pendown()
    turtle.color(color, color)
    turtle.begin_fill()
    turtle.goto(pt3)
    turtle.goto(pt1)
    turtle.goto(pt4)
    turtle.goto(pt2)
    turtle.goto(pt5)
    turtle.end_fill()

def star(center_x, center_y, radius, big_center_x, big_center_y):
    turtle.penup()
    turtle.goto(center_x, center_y)
    turtle.pendown()
    turtle.left(turtle.towards(big_center_x, big_center_y) - turtle.heading())
    turtle.forward(radius)
    turtle.right(90)
    draw_star(turtle.pos().x, turtle.pos().y, radius, 'yellow')
    #draw_star(turtle.pos()[0], turtle.pos()[1], radius, 'yellow')

turtle.reset()
turtle.speed(0)
width = 180
height = 120
draw_rect(-width/2, height/2, 'red', width/2, -height/2)

pice = width/30
big_center_x = -width/3
big_center_y = height/4
star(big_center_x, big_center_y-1, pice*3, big_center_x, big_center_y)
star(-width/6, height*2/5, pice, big_center_x, big_center_y)
star(-width/10, height*3/10, pice, big_center_x, big_center_y)
star(-width/10, height*3/20, pice, big_center_x, big_center_y)
star(-width/6, height/20, pice, big_center_x, big_center_y)
