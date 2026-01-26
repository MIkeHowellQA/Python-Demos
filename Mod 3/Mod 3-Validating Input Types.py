while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        if age > 0:
            break
        else:
            print("Age must be positive")
    except ValueError:
        print("Please enter a valid number")
