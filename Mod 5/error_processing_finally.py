# What does finally really do?

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        return result
        print ("Hello there, I'm after the return")
    finally:
        # I WILL ALWAY RUN NO MATTER WHAT
        # finally always runs
        # Clean up code - code that removes
        # frees any resource required by the functions
        # operations e.g. close database connection, close file
        # delete files
        # Be careful that finally doesn't itself generate errors.
        # Vry useful when you have more than one resource
        # open at a time and one of the resources fails,
        # your finally statement must release the correctly allocated
        # resource without trying to release the faulty resource.
        print("FINALLY IS RUNNING")

print (divide(10,0))
print ("Is this still running? Yes, if you see this.")