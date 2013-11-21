from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

import math

't = turtle'
'n = number of lines return to center'
'x = n/3'
'length = raw input'

def koch(t, n):
	if n<3:
		fd(t, n)
		return
	x = n / 3
	angle = 60

	koch(t, x)
	lt(t, angle)
	koch(t, x)
	rt(t, angle*2)
	koch(t, x)
	lt(t, angle)
	koch(t, x)
	
bob.delay = 0

def snowflake2(t, n):
	koch(t, n)
	rt(t, 120)
	koch(t, n)
	rt(t, 120)
	koch(t, n)
	rt(t, 120)

snowflake2(bob, 300)

def snowflake(t, n):
	for i in range(3):
		koch(t, n)
		rt(t, 120)

bob.x = -150
bob.y = 90
bob.redraw()

snowflake(bob, 300)

world.mainloop()
wait_for_user()

