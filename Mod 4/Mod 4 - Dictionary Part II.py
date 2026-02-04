productRange = {"item1":32.99,"item2":45.99,"item3":22.99}
# hashtables = dictionary

watches = {
    1: {"brand": "Braun", "price_gbp": 56},
    2: {"brand": "Casio", "price_gbp": 85},
    3: {"brand": "Timex", "price_gbp": 120},
    4: {"brand": "Rotary", "price_gbp": 105}
}

print (watches[10]["brand"])
# Add an entry
watches[11] = {
    "brand": "Timex",
    "model": "Weekender",
    "price_gbp": 60
}

print (watches)

# Change price
#watches[2]["price_gbp"] = 90

watches[2].update({
    "price_gbp": 90,
    "strap_type": "NATO"
})

# delete item
#del watches[1]

# Another way
removed = watches.pop(1)
print(removed)

watches.clear()

# Get an item
#print (watches[2]["brand"])
#print (watches[2].get("brand", "Unknown"))

# You can use in to check if a key exists
if 4 in watches:
    print("Watch exists")

# Using for
for watch in watches.values():
    print(watch["brand"])

# Find watches under £500
cheap_watches = {
    k: v for k, v in watches.items()
    if v["price_gbp"] < 500
}

# Get brands only
brands = {v["brand"] for v in watches.values()}

# shallow copy
backup = watches
# real copy
backup = watches.copy()

# merge dictionary (brand new operator)
new_stock = {
    12: {"brand": "Orient", "price_gbp": 250}
}

watches |= new_stock   # Python 3.9+

# sort by price
for watch_id, watch in sorted(
    watches.items(),
    key=lambda item: item[1]["price_gbp"]
):
    print(watch_id, watch["brand"], watch["price_gbp"])

#List brands
brands = [v["brand"] for v in watches.values()]

#Sum values
total = sum(v["price_gbp"] for v in watches.values())
