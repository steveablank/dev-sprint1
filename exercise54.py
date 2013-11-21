# This is where Exercise 5.4 goes
# Name: Steve Blank

# 5.4.1) Write a function named is_triangle that takes three integers as arguments, and that prints either "Yes" or "No," depending on whether you can or cannot form a triangle from stocks with the given lengths.

import math

def is_triangle(a, b, c):
	if a > b + c:
		print 'No'
	elif b > a + c:
		print 'No'
	elif c > a + b:
		print 'No'
	else:
		print 'Yes'



# 5.4.2) Write a function that prompts the user to input three stick lengths, converts them to integers, and uses is_triangle to check whether sticks with the given lengths can form a triangle.

def stick_triangle():
	a = int(raw_input('Enter the length of stick 1:'))
	b = int(raw_input('Enter the length of stick 2:'))
	c = int(raw_input('Enter the length of stick 3:'))

	print "Can your sticks form a triangle?"
	is_triangle(a,b,c)

stick_triangle()
