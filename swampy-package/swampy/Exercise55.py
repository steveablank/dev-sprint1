from TurtleWorld import *                 
world = TurtleWorld()                        
bob = Turtle()   

import math

'n = number of lines return to center'
'length = raw input'

def draw(t, length, n):
	if n == 0:
		return
	angle = 60
	fd(t, length*n)
	lt(t, angle)
	draw(t,length, n-1)
	rt(t, 2*angle)
	draw(t,length, n-1)
	lt(t, angle)
	bk(t, length*n)

bob.delay = 0.001

draw(bob, 8,5)

wait_for_user()
