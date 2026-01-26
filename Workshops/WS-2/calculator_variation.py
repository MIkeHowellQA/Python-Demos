def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def modulo(x,y):
    return x % y

def floordivision(x,y):
    return x // y

def power(x,y):
    return x ** y

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "%" : modulo,
    "//": floordivision, 
    "**": power,
    }

while True:
    while True:
        try:
            x = float(input ("Enter your first number:"))
            break
        except Exception as ex:
            print ("You entry is not a valid number, try again")
       

    while True:
        try:
            y = float(input ("Enter your second number:"))
            break
        except Exception as ex:
            print ("You entry is not a valid number, try again")
        
    while True:
        op = input("Enter an operation of either +, -, *, /, %, //, **:")
        if op in ["+", "-", "*", "/", "%", "//", "**"]:
            break
    
    result = operations[op](x, y)

    print (f"{x:g}{op}{y:g}={result:g}")

