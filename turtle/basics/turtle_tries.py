import turtle


def do_init(speed=3, start_x=-100, start_y=100):
    pen = turtle.Turtle()
    pen.speed(speed)
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    # pen.setx(start_x)
    # pen.sety(start_y)
    return pen


def do_square(pen):
    for i in range(4):
        pen.forward(150)
        pen.right(90)


turtle_window = turtle.Screen()
turtle_pen = do_init(2, 0, 0)
print(f'{turtle_pen.speed() = }')

print(f'{turtle_pen.xcor() = }, {turtle_pen.ycor() = }')
do_square(turtle_pen)
print(f'{turtle_pen.xcor() = }, {turtle_pen.ycor() = }')

turtle.done()
