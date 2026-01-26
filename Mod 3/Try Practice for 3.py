def addTwoNumbers(x, y):
    print (f"Your two numbers are x = {x} y = {y}")
    result = x + y
    return result

print (addTwoNumbers(50, 30))

mydict = {
    "usd": {"usd": 1.2, "gbp": 1, "zar": 26.1},
    "gbp": {"usd": 9, "gbp": 1, "zar": 30},
    "zar": {"usd": 1.2, "gbp": 1, "zar": 26.1}
}

list = ["Mike", "Robyn", "Banana Bread"]

print (mydict["gbp"]["zar"])