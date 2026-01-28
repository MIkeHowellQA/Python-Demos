# What does finally really do?

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        return result
    finally:
        print("FINALLY IS RUNNING")

print (divide(10,2))
print ("Is this still running? Yes, if you see this.")