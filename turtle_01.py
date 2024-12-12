# Importing Turtle
import turtle

# Initializing a pen
puskar = turtle.Turtle()

#Move the pen forward
puskar.forward(100) 
# or puskar.fd(100)

#Move the pen Backwards
# puskar.back(100) 
# or puskar.bk(100) 
# or puskar.backward(100)

# Turn the pen right by angle units
puskar.right(45)
# or puskar.rt(45)
puskar.forward(50) 

# Turn the pen left by angle units
puskar.left(45)
# or puskar.lt(45)
puskar.forward(50)

# Move turtle to an absolute position. If the pen is down, draw line. Do not change the turtle’s orientation.
# puskar.goto(100,200)
# or puskar.setposition(120, 200)
# or puskar.setpos(130, 200)

# Move turtle to an absolute position. Unlike goto(x, y), a line will not be drawn.
# turtle.teleport(100)
# turtle.teleport(x=100, y=100)

# Set the turtle’s first coordinate to x, leave second coordinate unchanged.
# puskar.setx(100)

# Set the turtle’s second coordinate to y, leave first coordinate unchanged.
# puskar.sety(100)

# Set the orientation of the turtle to to_angle.
# puskar.setheading(0) 
# or puskar.seth(to_angle)
puskar.setheading(90)
# puskar.setheading(180)
# puskar.setheading(270)

# Move turtle to the origin – coordinates (0,0) – and set its heading to its start-orientation (which depends on the mode, see mode()).
turtle.home()

# turtle.circle(radius, extent=None, steps=None)
puskar.circle(40, 180,100)

# Keep the animation window open
turtle.done()