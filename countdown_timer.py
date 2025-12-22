#This is my third project. This is a countdown timer that counts down from a user-specified number of seconds.
# I know its a simple project compared but I think its a good way to practice using loops and time module in python.
import time #Importing the time module to use its sleep function for creating delays in the countdown.
#according to python documentation, time.sleep() suspends execution for the given number of seconds.I myself will be finding out how it works as well.

#time.sleep(3) #Just to test if the module works.
#print("That is how this function works."). From what i have seen this function delays the execution of the print statement by an x amount of seconds as specied by me.

#Now i can confidently proceed to write the countdown timer code.
#For the sake of extra information, ChatGPT and Tiktok are great for getting beginner friendly projects to work on.

seconds = int(input("Enter the number of seconds for the countdown: "))
if seconds < 0:
    print("Time cannot be negative")
    exit()
for x in reversed(range(0, seconds)):
    print(x)
    time.sleep(1)  #Pausing the execution for 1 second in each iteration to create the countdown effect.
import colorama  #I like flashy output. Gives me a sense of accomplishment.
from colorama import Fore, Style 
print(Fore.GREEN + "happy new year!".upper())  #I tried to output in a gold colour and i quickly realised that there is no gold colour in colorama.
#So i settled for green because after reading up how to get gold in terminal output, it seemed too complicated for a beginner level project and I'm also not that guy.
#Maybe in future projects i will try to implement more complex colour schemes. 
print(Style.RESET_ALL)  #Vs code suggested this line to reset the style back to default after using colorama( i guess thats a good practice to follow).


#Thats a wrap for this project. I thought this would be more complex, this was quite the anticlimatic experience.
#But hey, its a learning experience after all. On to the next one!