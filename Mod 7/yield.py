
def hifi_brands():
    yield "Sony"
    yield "Technics"
    yield "Pioneer"
    yield "Yamaha"
    yield "Marantz"

for brand in hifi_brands():
    print(brand)


"""
### pause and resume effect
def hifi_brands():
    print("Starting generator")
    yield "Sony"
    print("Next brand...")
    yield "Technics"
    print("Next brand...")
    yield "Pioneer"
    print("Generator finished")

brands = hifi_brands()

print(next(brands))
print(next(brands))
print(next(brands))
"""

"""
### yield versus return
#def hifi_brands():
#    return ["Sony", "Technics", "Pioneer"]

### This allows one value to be returned at a time, it is a lazy algorithm.
def hifi_brands():
    for brand in ["Sony", "Technics", "Pioneer"]:
        yield brand

for brand in hifi_brands():
    print (brand)
"""

## Filter out brands from 80's and 90's
brands = [
    ("Sony", "80s"),
    ("Technics", "80s"),
    ("NAD", "90s"),
    ("Denon", "90s"),
    ("Beats", "2010s"),
]

def hifi_brands_80s_90s(brands):
    for name, era in brands:
        if era in ("80s", "90s"):
            yield name

for brand in hifi_brands_80s_90s(brands):
    print(brand)

