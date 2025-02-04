import random
import turtle as t

from wsgiref.validate import header_re
t.colormode(255)

tim_zolw = t.Turtle()
tim_zolw.shape(("turtle"))
tim_zolw.color("green3")

def random_color():
	r = random.randint(0,255)
	g = random.randint(0, 255)
	b = random.randint(0,255)
	random_color = (r,g,b)
	return random_color


colours = ["CadetBlue","green2","yellow","red","cyan1","DarkBlue","DarkOrange3","DimGrey","magenta2","gold2","RosyBrown","tan3","violet","wheat"]
def draw_shape(num_sides):
	angle = 360 / num_sides
	for _ in range(num_sides):
		tim_zolw.left(angle)
		tim_zolw.forward(100)

# for shape_side in range(3,11):
# 	tim_zolw.color(random.choice(colours))
# 	draw_shape(shape_side)


# def random_wal(num_steps):
# 	angles = [90, 180]
# 	directions = [0, 90, 180, 270]
# 	for _ in range(0,num_steps):
# 		tim_zolw.color(random_color())
# 		dir_choice = random.choice(directions)
# 		tim_zolw.setheading(dir_choice)
# 		step= random.randint(1,100)
# 		tim_zolw.forward(30)

def circle(gap_size):
	for _ in range(int(360 / gap_size)):
		tim_zolw.color(random_color())
		tim_zolw.circle(100)
		tim_zolw.setheading(tim_zolw.heading() + gap_size )
tim_zolw.speed(200)
circle(5)

#random_wal(200)

screen = t.Screen()
screen.exitonclick()