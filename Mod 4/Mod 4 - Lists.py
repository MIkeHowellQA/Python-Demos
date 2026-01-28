shopping = ["Eggs", "Banana", "Milk", "Onion", "Rice", "Banana"]

#print (shopping)
#print (shopping[3])
# start index: end index (not inclusive): step
#print (shopping[2: 4: 1])
#print (shopping[4: 1: -1])
#print (shopping[::-1])

shopping[2] = "Coffee"
print (shopping)

shopping.append("Pepper")
x = shopping.pop(3)
#print (shopping)

shopping.remove("Banana")
shopping.remove("Banana")

#print (shopping)

