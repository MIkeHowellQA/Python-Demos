data = {
    'names':["Mike", "Sam", "Mary"],
    'age': [23,27,24]
}

name_list = data["names"]

for name in name_list:    
    print (name)

##############################################

print (data["age"][1])

people= [
    {"name":"Peter", "age": 56},
    {"name":"Mike", "age": 34},
    {"name":"Tania", "age": 42}
]

print (people[2]["age"])

print ("Pre Bob") 

for person in people:
    print (person["name"])

print ("After Bob") 

people.append({"name":"Bob", "age": 32})

for person in people:
    print (person["name"])
"""
while True:
    display_summary_data()
    choice = get_menu_item()
    print ("Menu")
    print ("1. Details")
    print ("2. Add new person")

    choice = int(input ("Choose an option"))

    if choice == 1:
        ### Code to get details
        print ("Get detail")
        
        asdfdsa
        asdfasdf
        asdf
        asdf
        asdf
        asdf
        asdfasdf

    elif choice == 2:
        ### code to add a person    
        print ("Add a person")
        asdf
        asdf
        asdf
        asdf

    elif choice == 0:
        break
    else:
        print ("No such option")
"""

def ShowSummaryData():
    for person in people:
       print (person["name"], person["age"])

print ("1. Get details")
print ("2. Add a student")
print ("3. Edit a student")       
print ("4. delete a student")
print ("5. Display records")
print ("0. Exit")

