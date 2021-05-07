import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Sample
## Move back without drawing anything
#amy.penup()
#amy.forward(-140)
#amy.pendown()

## Draw three shapes of different colors, with space in between
#for prettycolor in ["red", "orange", "yellow"]:
#  amy.color(prettycolor)
#  amy.forward(50)
#  amy.penup()
#  amy.forward(50)
#  amy.pendown()

# Move back without drawing anything
amy.penup()
amy.forward(140)
amy.pendown()

# Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
  amy.color(prettycolor)
  for side in [1, 2, 3, 4]:
      amy.forward(50)
      amy.right(90)
  amy.penup()
  amy.forward(100)
  amy.pendown()