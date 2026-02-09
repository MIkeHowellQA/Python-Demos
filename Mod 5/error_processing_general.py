# General error handler

"""
while True:
    try:
        age = int(input("How old are you? "))
    except ValueError:
        print("That is not a valid age.")
    except FileNotFoundError:
        print ("alsdjfaklsdjflkasdjflkajsdflkj")
    else:
        print(f"You will be {age+5} in five years' time")
        break
"""

while True:
    try:
        age = int(input("How old are you? "))
    except Exception as ex:
        print("That is not a valid age.")
        print (ex)
        print (type(ex))
        print (type(ex).__name__)
        print(ex.__class__.__module__)
        print (ex.__traceback__.tb_lineno)
    else:
        print(f"You will be {age+5} in five years' time")
        break
