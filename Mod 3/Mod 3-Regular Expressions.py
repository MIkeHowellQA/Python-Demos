import re

email = input("Enter you email:")

if re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email):
    print ("valid email")
else:
    print ("Invalid email format")

            