try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print (f"The answer is {result}.")
finally:
    print("End of program.")

print ("Is this still running? Yes, if you see this.")