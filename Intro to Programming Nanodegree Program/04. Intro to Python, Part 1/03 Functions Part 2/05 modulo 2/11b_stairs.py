# Write code to draw the staircase
# pattern above.  The modulo operation
# might be useful!

import turtle
t = turtle.Turtle()
t.width(5)
t.color("limegreen")

for step in range(21):
    t.forward(10) 

    if step % 2 == 0:
        t.left(90)
    else:
        t.right(90)

t.hideturtle()