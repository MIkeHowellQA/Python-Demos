#print (10 / 0)

#int("abc")

#open("missing.txt")

## Slide 2

from asyncio.windows_events import NULL
import sys
"""
try:
    open ("missing.txt")
except FileNotFoundError:
    print ("I couldn't find the file")

print ("I'm still running your code...")
sys.exit()
"""

## Slide 2b
"""
try:
    open ("missing.txt")
    #print (10/0)
except FileNotFoundError:
    print ("I couldn't find the file")
except ZeroDivisionError:
    print ("No dividing by zero thank you!")

print ("I'm still running your code...")
sys.exit()
"""

## Slide 3
"""
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input.")
else:
    print("Age accepted.")    
finally:
    print("Input attempt finished.")
"""

## Slide 3b - Finally always runs, even after a return

"""
def divide(a,b):
    try:
        return a/b
    finally:
        print ("The finally part runs if the function returns successfully or fails.")

print (divide(10,2))
"""

## Slide 3c - Realistic use of finally in a function that writes to two files at the same time.
"""
def write_two_files():
    file_data = NULL
    file_log = NULL
    
    try:
        file_data = open("data.txt", "+w")
        file_log = open("p:log.txt", "+w")
        
        file_data.write ("Some data")
        file_log.write ("Log data")
    except Exception as ex:
        print (f"An error occured: {str(ex)}")
    finally:
        if file_data != NULL:
            file_data.close()
        if file_log != NULL:
            file_log.close()

write_two_files()
"""

## Slide 4
## Create your own custom errors
class InvalidScore(Exception):
    pass

def enter_score(score):
    if score < 0 or score > 100:
        raise InvalidScore("Score must be between 0 and 100.")
    print (f"Your score is {score}")

try:
    enter_score(120)
except InvalidScore:
    print ("Your score is out of range")
    