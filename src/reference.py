import turtle

t = turtle.Turtle()
t.speed(3)
t.pensize(4)

# Move to starting position
t.penup()
t.goto(-50, -100)
t.pendown()

# Left slanted line
t.left(75)
t.forward(200)

# Right slanted line
t.right(150)
t.forward(200)

# Middle bar
t.backward(100)
t.right(105)
t.forward(55)

turtle.done()
