# turtle graphic - window size

import turtle
turtle.setup(500, 500, 100, 100)    # width, height, start_x, start_y
win_width = turtle.window_width()
win_height = turtle.window_height()
margin = 50
x_max = int(win_width) // 2 - int(margin)
y_max = int(win_height) // 2 - int(margin)
t = turtle.Turtle()
#t.shape("turtle")
# shape can be 'arrow', 'classic', 'turtle', 'triangle', 'square' or 'circle'
t.shape('classic')

radius = 5
t.write("({}, {})".format(0, 0))
t.goto(-x_max, 0); t.dot(radius, 'red')
t.write("({}, {})".format(-x_max, 0))
t.goto(x_max, 0); t.dot(radius, 'red')
t.write("({}, {})".format(x_max, 0))
t.penup(); t.goto(0, y_max); t.pendown(); t.dot(radius, 'red')
t.write("({}, {})".format(0, y_max))
t.goto(0, -y_max); t.dot(radius, 'red')
t.write("({}, {})".format(0, -y_max))
t.penup(); t.goto(0, 0)