#!/usr/bin/python
# -*- coding: utf-8 -*-

# Marina Martín Hernández
# Ejercicio 13.5:

import sys

correct = False

if len (sys.argv) == 4:
	correct = True
	function = sys.argv[1]
	element1 = sys.argv[2]
	element2 = sys.argv[3]
	
def calculator (function, element1, element2):
	if function == 'add':
		return int(element1) + int(element2)
	elif function == 'sub':
		return int(element1) - int(element2)
	elif function == 'mult':
		return int(element1) * int(element2)
	elif function == 'div':
		try:
			return int(element1) / int(element2)
		except ZeroDivisionError:
			print("ERROR. You're trying to divide by 0.\n")
	else:
		return "ERROR. Insert the correct operator: add, sub, mult, div.\n"


if __name__ == "__main__":
	if correct:
		try:
			print (calculator(function, element1, element2))
		except ValueError:
			print ("Error. Insert numbers for operate.")
	else:
		print ("Error. Insert the correct parameter.")