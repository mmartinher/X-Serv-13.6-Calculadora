#!/usr/bin/python

import sys

correct = False

if len (sys.argv) == 4:
    correct = True
    operator = sys.argv[1]
    number1 = sys.argv[2]
    number2 = sys.argv[3]

def calculator (num1, num2, operator):
    if operator == 'add':   #ADDITION
        return int(num1) + int(num2)
    elif operator == 'sub': #SUBTRACTION
        return int(num1) - int(num2)
    elif operator == 'mult': #MULTIPLICATION   
        return int(num1) * int(num2)
    elif operator == 'div': #DIVISION
        try:
            return int(num1) / int(num2)
        except ZeroDivisionError:
            print "Error. You're trying to divide by 0."
    else:
        return "Error. Insert the correct operator: sum, sub, mult, div."


if __name__ == "__main__":
    if correct:
        try:
            print (calculator(number1, number2, operator))
        except ValueError:
            print "Error. Insert numbers for operate."
    else:
        print "Error. Insert the correct parameter."
