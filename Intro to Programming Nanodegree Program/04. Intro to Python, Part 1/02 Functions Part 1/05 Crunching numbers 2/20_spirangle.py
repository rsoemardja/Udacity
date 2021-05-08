# Sample
#import turtle
#t = turtle.Turtle()
#t.color("cyan")

#for side in range():
#    t.forward()
#    t.right(120)

import turtle

def spiral():
    t = turtle.Turtle()
    t.color("cyan")
    for n in range(100):
        t.forward(n)
        t.right(20)

spiral()