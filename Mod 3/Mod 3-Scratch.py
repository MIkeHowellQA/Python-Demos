# Some changes
# More changes
"""
rain = True
  if rain:
    print("Remember to take an umbrella.")
else:
    print("You don't need an umbrella.")

hungry = True

if hungry:
    print("I am hungry..Feed me!")
else:
    print("I am full.  No need for food yet!")

rain = True
money = False

if rain:
    if money:
        print("Take the bus.")
    else:
        print("Walk but take an umbrella.")
else:
    if money:
        print("Take the bus if you're feeling lazy")
    else:
        print("Walk, but You don't need an umbrella.")    

my_money = 9

if my_money > 10:
    print("You have sufficient funds in your account.")
else:
    print("There is not enough money in your account to complete the purchase.")


deposit = 100

if 0 < deposit <= 100:
    print(f"Thank you for the £{deposit} deposit!")
else:
    print("This is not a valid amount to deposit.")    

deposit = 150

#if 0 < deposit <= 100:
if deposit > 0 and deposit <= 100:
    print(f"Thank you for the £{deposit} deposit!")
else:
    print("This is not a valid amount to deposit.")    

#Students at a secondary school have to take an end of term test.
#In order to pass they need to answer 20 out of 30 questions correctly.
#Write a program which asks a student to input their score. 
#then use a comparator conditional to check whether they have passed.
#Then output a message informing the student whether they passed or failed.

result = int(input("Enter your mark:"))
if result >= 20:
    print ("Passed")
else:
    print ("Failed")

deposit = 100
password = "password"

if (0 < deposit <= 100 and password == "password") or (password=="THEBOSS"):
    print(f"Thank you for depositing £{deposit}!")
else:
    print("Failed to make a deposit.")

age = int(input("Enter your age: ")) 

if age >= 85:   
  print("You are above 85")
elif age >= 50:   
  print("You are between 50 and 85")
elif age >= 20:   
  print("You are between 20 and 50")
else:    
  print("You are below 20 years old")

## elif is what we call syntactic sugar---it has no need to exist--it just looks good
if age >= 85:   
  print("You are above 85")
else:
  if age >= 50:   
    print("You are between 50 and 85")
  else:
    if age >= 20:   
       print("You are between 20 and 50")
    else:    
       print("You are below 20 years old")

#The students in a class take a test that asks 70 questions. 
# Each student receives a grade based on the percentage of questions they answered correctly:
# Pass with distinction: 80% and over
# Pass with merit: 60-79%
# Pass: 50-59%
# Fail: Less than 50%

mark=90
if mark >= 80:
    print ("distinction")
elif mark >= 60:
    print ("merit")
elif mark >= 50:
    print ("pass")       
else:
    print ("fail")    

register= ["Khaled", "Rob", "Sally", "Ash"]
name = input ("Type in your name:")
if name not in register:
    print ("Welkomen!")
else:
    print ("Tschus!")

"""
#Create an odd-one-out game using a list conditional.

#Print your questions to the terminal. For example: What is the odd one out: apple, banana, orange, potato.
#Create a list with the three elements that are in a group
#Ask the user to input their answer.
#Print out an appropriate message if the user guesses correctly or incorrectly.
#For an extra challenge, change the user input so it always matches the case of the strings (you’ll need to find the right string method to use). Also, what happens if someone doesn’t provide a valid answer to the question?


items=["apple", "banana", "orange"]
guess=input("What is the odd one out? apple, banana, orange, potato: ").lower()
#guess = guess.lower()
if guess in items:
    print ("That is on the list!")
else:
    if guess == "potato":
        print ("That is the odd one out!")
    else:
        print ("I have no idea what that is!  Is that even a fruit?")

