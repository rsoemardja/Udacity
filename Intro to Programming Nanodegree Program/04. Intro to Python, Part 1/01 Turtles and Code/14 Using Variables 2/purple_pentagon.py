#sample
#import turtle
#mary = turtle.Turtle()
#mary.color("purple")
#for side in [1, 2, 3, 4, 5]:
#    mary.forward(100)
#    mary.right(72)

#solution
import turtle
mary = turtle.Turtle()
mary.color("purple")
color = "purple"
sides = [1, 2, 3, 4, 5]
angle = 72
distance = 100
mary.color(color)
for side in sides:
    mary.forward(distance)
    mary.right(angle)