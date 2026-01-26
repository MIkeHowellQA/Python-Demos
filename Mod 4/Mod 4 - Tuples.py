marks = (56, 39, 63, 49, 28)

print (marks[3])

print (marks[1:4])

# This won't work
#marks[3] = 5

marks = marks + (60,40,)
print (marks)

print (63 in marks)

# unpacking
first, *middle, last = marks
print (middle)

# tuples can be keys
results = {
    ("Alice", "Maths"): 56,
    ("Alice", "Biology"): 89,

    ("Bob", "Maths"): 39
}

# Create a new tuple based on a condition applied to an existing tuple
passed = tuple(m for m in marks if m >= 40)
print (passed)
