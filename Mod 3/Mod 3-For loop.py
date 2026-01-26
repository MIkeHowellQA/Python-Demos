print ("range(5):")
for i in range(5):
    print (i)

print ("range(1,6):")
for i in range(1,6):
    print (i)    


print ("range(10,-10, -2):")
for i in range(10,-10,-2):
    print (i)    

print ("Iterable object: string")
for letter in "hello":
    print (letter)   



# List comprehensions
steps = 0.25
vals = [i * steps for i in range(0, int(2.0 / steps) + 1)]
print(vals)
