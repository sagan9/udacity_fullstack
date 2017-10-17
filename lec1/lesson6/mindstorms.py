import turtle

def draw_square(some_turtle, initial_angle=0):
    some_turtle.right(initial_angle)
    for cnt in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)
    some_turtle.home()

def draw_triangle(some_turtle, initial_angle=0):
    some_turtle.right(initial_angle)
    for cnt in range(3):
        some_turtle.forward(100)
        some_turtle.right(120)
    some_turtle.home()

screen = turtle.Screen()
screen.bgcolor('red')

brad = turtle.Turtle()
brad.shape('turtle')
brad.color('yellow')
brad.speed(10)

for angle in range(36):
    draw_square(brad, angle*10)