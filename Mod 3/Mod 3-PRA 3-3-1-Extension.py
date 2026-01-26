## Practice activity 3.3.1 with extension task from SEF
conversion_factors = {   
    "USD": {"GBP": 0.71, "EUR": 0.83, "JPY": 109.23},   
    "GBP": {"USD": 1.41, "EUR": 1.17, "JPY": 151.57},    
    "EUR": {"USD": 1.21, "GBP": 0.85, "JPY": 130.59},    
    "JPY": {"USD": 0.0092, "GBP": 0.0066, "EUR": 0.0076}}

def convert_currency(amount, source_currency, target_currency):
  return conversion_factors[source_currency][target_currency]


while True:
    while True:
        try:
            amount = float(input("Enter an amount: "))
            break
        except:
            print ("That wasn't a number, try again.")    

    while True:
        while True:
            try:
                srcCurrency = input ("What currency is that amount in (GBP, USD, EUR or JPY) ?").upper()
                conversion_factors[srcCurrency]
                break
            except:
                print ("I don't recognize that source currency, try again.")
            
        while True:
            try:
                destCurrency = input ("What currency do you want to convert that to (GBP, USD, EUR or JPY)?").upper()
                conversion_factors[srcCurrency][destCurrency]
                break
            except:
                print ("I don't recognise that currency as a destination, try again.")        
        
        break

    print (f"The {amount:.2f} converted to {destCurrency} is {convert_currency(amount, srcCurrency, destCurrency):.2f}")

    while True:
      answer = input ("Do you want to convert another amount (yes or no)?").upper()
      if answer == "YES":
          break
      elif answer == "NO":
          exit()
      else:
          print ("You must choose between 'yes' or 'no.  Try again.")