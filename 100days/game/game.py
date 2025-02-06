import random
from turtle import Turtle,Screen

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Wihc turtle will win the race? Enter a color:")
colors=["red","orange","yellow","green","blue","purple"]
is_race_on= False
y=-150
all_turtles=[]
for _ in range(0,6):
	tim_ = Turtle(shape="turtle")
	tim_.color(colors[_])
	tim_.shapesize(2)
	tim_.penup()
	tim_.goto(-230,y)
	y+=60
	tim_.speed(20)
	all_turtles.append(tim_)
if user_bet:
	is_race_on = True
while is_race_on:
	for turtle in all_turtles:
		if turtle.xcor() >230:
			winning_color = turtle.pencolor()
			is_race_on = False
			if winning_color == user_bet:
				print(f"You have won, the winning color is: {winning_color}")
			else:
				print(f"You have lose, the winning color is: {winning_color}")
		random_distance = random.randint(0, 10)
		turtle.forward(random_distance)




screen.exitonclick()