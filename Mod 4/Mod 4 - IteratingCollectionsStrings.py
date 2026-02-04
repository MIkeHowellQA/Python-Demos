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

# when you apply for to a dictionary, the loop iterates
# through the keys
# (be careful of example on book, price points to keys not price)
for price in productRange:
    print(f"The price of {price} is £{productRange[price]}.")

for key in productRange:
    print(f"The price of {key} is £{productRange[key]}.")   
    
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
