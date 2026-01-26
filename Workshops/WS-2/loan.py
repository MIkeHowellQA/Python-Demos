while True:
    salary = float(input("Salary:"))
    age = int(input("Age:"))
    credit_score = int(input("Credit score:"))

    if salary < 25000:
      print ("Salary is too low.")
    elif not(21 <= age <= 60):
        print ("You are out of the age range")
    elif credit_score < 650:
      print ("Credit score is too low")
    elif 650 <= credit_score < 700:
        guarantor = input("Do you have a guarantor?").lower()
        if guarantor == "n":
          print ("You need a guarantor.")
        else:
          print ("You qualify by the skin of your teeth.")
    else:
        print ("You qualify")

    another = input ("Do you want to check another application (y/n)?").lower()
    if another == "n":
       break