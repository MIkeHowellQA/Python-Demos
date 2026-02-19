data = "my data"
x = "strawberry"

def function_one():
    # take the global version of x
    global x
    # local variable - once you leave function one it ceases
    # to exist (like the parrot).
    x = "Banana"
    
    print (x)
    print (data)

def function_two():
    # Take the local version of x
    # x = 99
    print (x)
    print (data)


function_one()
function_two()

