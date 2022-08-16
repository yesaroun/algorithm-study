import turtle
turtle.setup(500, 500, 100, 100)
t = turtle.Pen()
t.shape("turtle")
t.pensize(10)
t.pencolor("red")
t.speed(1)

side = 200
turn_angle = 120
t.forward(side)
t.left(turn_angle)
t.forward(side)
t.left(turn_angle)
t.forward(side)
t.left(turn_angle)
t.forward(side)
t.left(turn_angle)
turtle.mainloop()