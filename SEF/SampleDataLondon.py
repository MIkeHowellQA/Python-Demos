data = {
    'names': ['Mike', 'Sam', 'Mary'],
    'ages' : [27, 23, 24],
    'majors' : [['comp sci', 'physics'], ['botany', 'chemistry'], ['psychology', 'linguistics']]
}

students = [
        {'name' : 'Mike', 'age':27, 'majors':['comp sci', 'physics']},
        {'name' : 'Sam', 'age':23, 'majors':['botany', 'chemistry']},
        {'name' : 'Mary', 'age':24, 'majors':['psycho', 'linguistics']}    
]

# age of the 3rd student
#print (students[2]['age'])

# \n linefeed
for student in students:
    print (f"""name:{student['name']}
age: {student['age']}
""")

"""
print (data['names'][2])

names = data['names']
for name in names:
    print (name)

"""

def get_menu_choice():
    print ("Menu")

    print ("1. Add records")
    print ("2. Amend records")
    print ("3. Delete records")
    print ("4. Display records")
    print ("0. Exit")

    choice = int(input("Choose a menu item:"))
    return choice

def add_new_student():
    print ("Add a new student")

def amend_student():
    print ("Amend student")

def delete_student():
    print ("Delete student")

    
def display_student():
    print ("Display student")

## Main body
while True:
    #display_data_summary()
    option = get_menu_choice()
    
    if option == 1:
        add_new_student()
    elif option == 2:
        amend_student()
    elif option == 3:
        delete_student()
    elif option == 4:
        display_student()
    elif option == 0:
        break
    else:
        print ("No such option")