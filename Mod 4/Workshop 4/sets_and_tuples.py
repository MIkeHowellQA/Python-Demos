fruits = {"grape", "orange", "pear", "fig", "granadilla"}

print (fruits)

fruits.add ("blueberry")
fruits.remove ("pear")

print (fruits)
print ()

rectangleDimensions = (400, 900)

print (f"width = {rectangleDimensions[0]} height = {rectangleDimensions[1]}")

## Extension

moreFruit = {"tangerine", "orange", "strawberry", "lemon", "pear", "fig"}

print(f"""
  Your first fruit set {fruits}
  Your second fruit set {moreFruit}
""")

print ("The union of your fruit " + str(fruits | moreFruit))
print ("The intersection of your fruit " + str(fruits & moreFruit))
print ("The difference by taking the second set from the first " + str(fruits - moreFruit))

print()

try:
    rectangleDimensions[0] = 450
except Exception as error:
    print ("You cannot change your rectangle's dimensions: " + str(error))





