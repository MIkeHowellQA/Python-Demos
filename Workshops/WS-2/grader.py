"""
while True:
  try:
    s = int(input("Enter your score:"))

    if s < 0 or s > 100:
      print ("I can't do anything with scores outside 0-100.")
    else:
      if s >= 90:
        grade = "A"
      elif s >= 80:
        grade = "B"
      elif s >= 70:
        grade = "C"
      elif s >= 60:
        grade = "D"
      elif s >= 50:
        grade = "E"
      else:
        grade = "Failed"
        
      print (f"Your grade is {grade}")
  except Exception as ex:
    print (f"Your error is: {ex}")
"""

while True:
  try:
    s = int(input("Enter your score:"))

    if s < 0 or s > 100:
      print ("I can't do anything with scores outside 0-100.")
    else:
        match s:
            case x if x >= 90:
                grade = "A"
            case x if x >= 80:                
                grade = "B"
            case x if x >= 70:
                grade = "C"
            case x if x >= 60:
                grade = "D"
            case x if x >= 50:
                grade = "E"
            case _:
                grade = "Failed"           
        print (f"Your grade is {grade}")
        
  except Exception as ex:
    print (f"Your error is: {ex}")




        