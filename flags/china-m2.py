import turtle
import time
import os

def  draw_square(org_x, org_y, x, y):
    turtle.setpos(org_x, org_y)  # to left and bottom connor
    turtle.color('red', 'red')
    turtle.begin_fill()
    turtle.fd(x)
    turtle.lt(90)
    turtle.fd(y)
    turtle.lt(90)
    turtle.fd(x)
    #print(turtle.pos())
    turtle.lt(90)
    turtle.fd(y)
    turtle.end_fill()
 
def draw_star(center_x, center_y, radius):
    print(center_x, center_y)
    turtle.pencolor('black')
    turtle.setpos(center_x, center_y)
    pt1 = turtle.pos()
    turtle.circle(-radius, 360 / 5)
    pt2 = turtle.pos()
    turtle.circle(-radius, 360 / 5)
    pt3 = turtle.pos()
    turtle.circle(-radius, 360 / 5)
    pt4 = turtle.pos()
    turtle.circle(-radius, 360 / 5)
    pt5 = turtle.pos()
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.goto(pt3)
    turtle.goto(pt1)
    turtle.goto(pt4)
    turtle.goto(pt2)
    turtle.goto(pt5)
    turtle.end_fill()
print(turtle.pos())
 
#turtle.pu()
draw_square(-320, -260, 660, 440)

 # big star center
star_part_x = -320
star_part_y = -260 + 440
star_part_s = 660 / 30
center_x, center_y = star_part_x + star_part_s * 5, star_part_y - star_part_s * 5
turtle.setpos(center_x, center_y) 
turtle.lt(90)
draw_star(star_part_x + star_part_s * 5, star_part_y - star_part_s * 2, star_part_s * 3)
 
# draw 1st small star
turtle.goto(star_part_x + star_part_s * 10, star_part_y - star_part_s * 2)    # go to 1st small star center
turtle.lt(round(turtle.towards(center_x, center_y)) - turtle.heading())
turtle.fd(star_part_s)
turtle.rt(90)
draw_star(turtle.xcor(), turtle.ycor(), star_part_s)
 
# draw 2nd small star
turtle.goto(star_part_x + star_part_s * 12, star_part_y - star_part_s * 4)    # go to 1st small star center
turtle.lt(round(turtle.towards(center_x, center_y)) - turtle.heading())
turtle.fd(star_part_s)
turtle.rt(90)
draw_star(turtle.xcor(), turtle.ycor(), star_part_s)
 
# draw 3rd small star
turtle.goto(star_part_x + star_part_s * 12, star_part_y - star_part_s * 7)    # go to 1st small star center
turtle.lt(round(turtle.towards(center_x, center_y)) - turtle.heading())
turtle.fd(star_part_s)
turtle.rt(90)
draw_star(turtle.xcor(), turtle.ycor(), star_part_s)
 
# draw 4th small star
turtle.goto(star_part_x + star_part_s * 10, star_part_y - star_part_s * 9)    # go to 1st small star center
turtle.lt(round(turtle.towards(center_x, center_y)) - turtle.heading())
turtle.fd(star_part_s)
turtle.rt(90)
draw_star(turtle.xcor(), turtle.ycor(), star_part_s)
turtle.ht()
done()
