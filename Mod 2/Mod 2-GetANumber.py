okay=False

while not okay:
    try:
      number = int(input("Enter a number:"))
      okay = True;
    except Exception as e:
       okay = False
       print (f"Error: that wasn't a number, try again\n{e}")

print (f"You entered the number {number}")

"""
######### Variation
while True:
    try:
      number = int(input("Enter a number:"))
      break
    except Exception as e:
       okay = False
       print (f"Error: that wasn't a number, try again\n{e}")
"""