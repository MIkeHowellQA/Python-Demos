## Practice activity 3.3.1 from SEF

while True:
    while True:
        try:
            amount = float(input("Enter an amount: "))
            break
        except:
            print ("That wasn't a number, try again.")
    

    while True:
      destCurrency = input ("Do you want to convert that to GBP or USD? ").upper()

      if destCurrency == "GBP":
          result = amount / 1.31
          break
      if destCurrency == "USD":
          result = amount * 1.31
          break

    print (f"The {amount:.2f} converted to {destCurrency} is {result:.2f}")

    while True:
      answer = input ("Do you want to convert another amount (yes or no)?").upper()
      if answer == "YES":
          break
      elif answer == "NO":
          exit()
      else:
          print ("You must choose between 'yes' or 'no.  Try again.")