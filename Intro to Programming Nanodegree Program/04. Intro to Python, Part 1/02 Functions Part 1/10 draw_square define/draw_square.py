# sample
#import turtle
#jack = turtle.Turtle()
#jack.color("yellow")

# answer
import turtle
jack = turtle.Turtle()
jack.color("yellow")
jack.speed(0)
def draw_square():
    for side in range(4):
        jack.forward(100)
        jack.right(90)
for square in range(80):
    draw_square()
    jack.forward(5)
    jack.left(5)
draw_square()