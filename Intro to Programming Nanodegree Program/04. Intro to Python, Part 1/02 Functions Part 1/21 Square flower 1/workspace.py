#import turtle

#def draw_square(some_turtle):
#    for side in range(4):
#        some_turtle.forward(100)
#        some_turtle.right(90)

#romeo = turtle.Turtle()
#romeo.color("violet")
#romeo.speed(8)
#for petal in range(6):
#    draw_square()
#    romeo.right(60)

#romeo.hideturtle()

#solution
import turtle

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

romeo = turtle.Turtle()
romeo.color("violet")
romeo.speed(8)
for petal in range(6):
    draw_square(romeo)
    romeo.right(60)
