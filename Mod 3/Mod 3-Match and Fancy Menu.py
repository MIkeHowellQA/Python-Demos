"""
while True:
    print ("1) Find customer by id")
    print ("2) Find customers by product purchased")
    print ("3) Find customers by spend amount")

    option = int(input("Enter your choice:"))

    match option:
        case 1:
            print ("*Finding customer by id*")
        case 2:
            print ("*Finding customers by product purchased*")
        case 3:
            print ("*Finding customers by product purchased*")
        case _:
            print ("*That isn't a valid option*")

#####################
## Check a range of values using match.
## case transfers the value into a variable and "guard" checks if it is range

value = 42

match value:
    case v if 0 <= v <= 10:
        print("Between 0 and 10")
    case v if 11 <= v <= 100:
        print("Between 11 and 100")
    case _:
        print("Out of range")
"""
###############
## A classic text based menu example implemented using a dictionary of tuples to store 
## the text for the menu items together with the function that runs the chosen item.
"""
def findCustomerbyId():
  print ("\n* Find customer by id *\n")

def findCustomerbyProduct():
  print ("\n* Find customer by product *\n")
     
def findCustomerbySpend():
  print ("\n* Find customer by spend *\n")

menu = {
    1: ("Find customer by id", findCustomerbyId),
    2: ("Find customer by product purchased", findCustomerbyProduct),
    3: ("Find customer by spend amount", findCustomerbySpend),
}

while True:
  for key, menuitem in menu.items():
    print (f"{key}. {menuitem[0]}")

  choice = int(input("Choose an option: "))

  menu[choice][1]()
"""    