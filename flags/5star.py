import uturtle
import math

turtle = uturtle.Turtle()

def draw_star(size, color):
    angle = 144
    turtle.fillcolor(color)
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()
    return

radius = 70
sl = math.cos(54.0 / 180.0 * math.pi) / math.cos(36.0 / 180.0 * math.pi) * radius
print(sl)
draw_star(sl, "yellow")
