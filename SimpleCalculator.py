import math # imports the math module for the power operation
import sys # imports the sys module for exiting the program

numbers = '0123456789' # a string of numbers
opertaions = '+-*/%**' # a string of operations

x = int(input("Enter a number (0 to 9): ")) # asks for a number
if x not in numbers: # if the number is not in the string of numbers
    print("Invalid number") # print "Invalid number"

y = int(input("Enter another number (0 to 9): ")) # asks for another number
if y not in numbers: # if the number is not in the string of numbers
    print("Invalid number") # print "Invalid number"

operation = input("Enter an operation (+,-,*,/,%,**): ") # asks for an operation
if operation not in opertaions: # if the operation is not in the string of operations
    print("Invalid operation") # print "Invalid operation"

if operation == "+":
    print(x + y) # if the user enters "+", then print the sum of x and y
elif operation == "-":
    print(x-y) # if the user enters "-", then print the difference of x and y
elif operation == "*":
    print(x*y) # if the user enters "*", then print the product of x and y
elif operation == '/':
    print(x/y) # if the user enters "/", then print the quotient of x and y
elif operation == '%':
    print(x%y)  # if the user enters "%", then print the remainder of x and y
elif operation == '**':
    print(x**y) # if the user enters "**", then print x to the power of y
else:
    print("Invalid operation") # if the user enters an invalid operation, then print "Invalid operation"
    sys.exit(1) # exits the program with an error code of 1



