# This is my second Python project. 
# It is an interest calculator that computes simple and compound interest based on user input.
#It steals from the similar concepts i used in my first project, a simple calculator.
#However this project is meant to be more of an experiment to see what else i can do with python.
# The code may be messy but hey its a learning experience.
import math
#Not too sure if i will be using this module but importing it just in case.

principal=float(input("Enter the principal amount:"))
if principal<=0:
    print("Principal  amount must be greater than zero.")
    exit()
rate=float(input("Enter the rate of interest:"))
if rate<=0 or rate>100:
    print("Rate of interest must be greater than zero and less than or equal to 100.")
    exit()

rate = rate / 100
time = float(input("Enter the time in years:"))
interest_type = input("Enter 'S' for Simple Interest or 'C' for Compound Interest:").upper()
if interest_type not in ['S', 'C']:
    print("Invalid interest type option.")
    exit()
#Now the aim of the code from this point onwards is to calculate either simple or compound interest based on user input.
#The idea is to use conditional statements to determine which calculation to perform.
if interest_type=='S':
    simple_interest=(principal*rate*time)
    total_amount=principal+simple_interest
    print(f"The Simple Interest is: {simple_interest}")
    print(f"The Total Amount after {time} years is: {total_amount}")
#Now here is where it may get messy, but bear with me.
# I will try to keep it as clean as possible.
# I want to account for real world scenerios whereby interest may be compounded daily, weekly, monthly, semi-annually or annually.    
elif interest_type=='C':
    compounded_frequency=input("Enter 'D' for Daily, 'W' for Weekly, 'M' for Monthly, 'S' for Semi-Annually or 'A' for Annually compounding:").upper()
#Since user input can be unpredictable I chose to convert the input to uppercase to avoid case sensitivity issues, since my options are all uppercase.
#.Upper() method converts any lowercase letters to uppercase.A foolproof string method if you ask me.
    if compounded_frequency=='D':
        n=365
    elif compounded_frequency=='W':
        n=52
    elif compounded_frequency=='M':
        n=12
    elif compounded_frequency=='S':
        n=2
    elif compounded_frequency=='A':
        n=1
    else:
        print("Invalid compounding frequency option.")
        exit()
    initial=principal*(math.pow((1+(rate/n)),(n*time)))
    compound_interest=initial-principal
#The math module comes in handy here for the power function. I tried usind the ** operator but it got messy with the order of operations.
#So i opted for the math.pow() function instead.Glad i did that. So now i know for future uses.
    total_amount=principal+compound_interest
    print(f"The Compound Interest is: {compound_interest}")
    print(f"The Total Amount after {time} years is: {total_amount}")