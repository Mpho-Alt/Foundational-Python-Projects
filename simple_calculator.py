# This is my first official program in python.
# The program is a simple calculator that can perform basic arithmetic operations.
# It takes two numbers and an operator as input from the user and displays the result.
# The is simple calculator is meant to demostrate a basic understating of basic conditional statements and user input handling in Python.
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
# I thought the addition of colour would make the program more interesting.
heading = "SIMPLE CALCULATOR"
print(Fore.CYAN + heading)

num_1 = float(input( "Enter first number: "))
operator = input(Fore.CYAN + "Enter operator (+, -, *, /, **): ")
num_2 = float(input("Enter second number: "))
if operator == "+":
    result = num_1 + num_2
    print(Fore.GREEN + f"{num_1} + {num_2} = {result}")
elif operator == "-":
    result = num_1 - num_2
    print(Fore.GREEN + f"{num_1} - {num_2} = {result}")
elif operator == "*":
    result = num_1 * num_2
    print(Fore.GREEN + f"{num_1} * {num_2} = {result}")
elif operator == "/":
    result = num_1 / num_2
    print(Fore.GREEN + f"{num_1} / {num_2} = {result}")
elif operator == "**":
    result = num_1 ** num_2
    print(Fore.GREEN + f"{num_1} ** {num_2} = {result}")
else:
    print(Fore.RED + "Invalid operator. Please use one of +, -, *, /, **.")