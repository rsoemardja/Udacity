mood = "happy"

import turtle
riley = turtle.Turtle()
riley.width(5)

# Add your code here.
 #solution with if statement
if mood == "happy":
    riley.color("yellow")
elif mood == "sad":
    riley.color("blue")
else:
    riley.color("gray")

for side in range(5):
    riley.forward(100)
    riley.right(144)