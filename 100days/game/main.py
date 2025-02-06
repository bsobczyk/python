from turtle import Turtle,Screen



tim = Turtle()
screen = Screen()

screen.listen()

def move_forwards():
	tim.forward(10)

def move_backwards():
	tim.backward(10)

def move_cclockwise():
	a = tim.heading()
	tim.setheading(a+10)

def move_clockwise():
	a = tim.heading()
	tim.setheading(a-10)



screen.listen()

screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=move_cclockwise)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="c", fun=tim.reset)

screen.exitonclick()