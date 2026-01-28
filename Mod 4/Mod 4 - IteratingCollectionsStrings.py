for char in "Hello class":
    print(char)

for char in "Hello class how are you?".split():
    print(char)    

# Apply FOR to a list
my_fruit = ["Apple", "Banana", "Orange"]

for fruit in my_fruit:
    print(fruit.upper())    

# Apply FOR to a dictionary
productRange = {"item1":32.99,"item2":45.99, "item3":25.99}

for price in productRange:
    print(f"The price of {price} is £{productRange[price]}.")

productRange = {"item1":32.99,"item2":45.99, "item3":25.99}

for price in sorted(productRange):
    print(f"The price of {price} is £{productRange[price]}.")

productRange = {"item1":32.99,"item2":45.99, "item3":25.99}

for price in sorted(productRange.values()):
    print(f"price={price}")

# Sort by value, include the key in the output
import operator
for k, v in sorted(productRange.items(), key=operator.itemgetter(1)):
     print(f"The price of {k} is £{v}.")
