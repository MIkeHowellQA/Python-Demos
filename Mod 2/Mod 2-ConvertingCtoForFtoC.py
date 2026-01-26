temp=input("Enter the temperature:")
unit=input("Is the temperature in C or F?")

try:
    unit=unit.lower()
    temp=float(temp)

    if (unit == "f"):
      result = (temp - 32) * 5/9
    else:
      result = (temp * 9/5) + 32

    print(f"The converted temperature is equal to {result:.1f}")
except Exception as e:
     print(f"You caused an {e} error.")