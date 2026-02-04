contacts={}

for num in range(1,4):
    contacts[f"Contact{num}"] = f"phone: 555-{str(num)*4}"

print (contacts)

for name, phone in contacts.items():
    print (f"{name} - {phone}")

"""
while True:
    try:
        name = input("Type in a contact name:")
        # try to access the name
        contacts[name]
        newNumber = input("Type in a new number for that contact:")
    except Exception as ex:    
        print ("Can't find that contact")
    else:
        contacts[name] = newNumber

    for name, phone in contacts.items():
        print (f"{name} - {phone}")  
"""

while True:
    name = input("Type in a contact name (q to quit):")

    if name.lower() == "q":
        break

    # try to access the name
    if not name in contacts:
        print ("No such contact")
        continue

    newNumber = input("Type in a new number for that contact:")
    contacts[name] = newNumber        

    for name, phone in contacts.items():
        print (f"{name} - {phone}")  