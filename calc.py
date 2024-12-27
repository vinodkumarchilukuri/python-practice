

import os
import sys

def addition(num1, num2):
    add = num1+num2
    return add

def subtraction(num1, num2):
    sub = num1-num2
    return sub

def mul(num1, num2):
    mult=num1 * num2
    return mult

def div(num1, num2):
    divi=num1 / num2
    return divi

num1=int(sys.argv[1]) # to take command line inputs
operation=sys.argv[2] # to take command line inputs
num2=int(sys.argv[3]) # to take command line inputs

print(os.getenv("password"))  #to print environment variables
 
if operation == "addition":
    output=addition(num1, num2)
    print(output)

if operation == "sub":
    output=subtraction(num1, num2)
    print(output)

if operation == "mul":
    output=mul(num1, num2)
    print(output)

if operation == "div":
    output=div(num1, num2)
    print(output)
