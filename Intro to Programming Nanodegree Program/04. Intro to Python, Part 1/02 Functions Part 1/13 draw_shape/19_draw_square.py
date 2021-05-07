# sample
#import turtle
#jack = turtle.Turtle()
#jack.color("yellow")

# answer
import turtle
jack = turtle.Turtle()

def draw_shape(length, color, sides):
    jack.color(color)
    for side in range(sides):
        jack.forward(length)
        jack.right(360/sides)

draw_shape(100, "cyan", 5)