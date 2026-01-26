watches = {
    1: {
        "brand": "Rolex",
        "model": "Submariner Date",
        "movement": "Automatic",
        "case_material": "Stainless Steel",
        "water_resistance_m": 300,
        "dial_color": "Black",
        "strap_type": "Bracelet",
        "price_gbp": 9200
    },
    2: {
        "brand": "Omega",
        "model": "Speedmaster Professional",
        "movement": "Manual",
        "case_material": "Stainless Steel",
        "water_resistance_m": 50,
        "dial_color": "Black",
        "strap_type": "Bracelet",
        "price_gbp": 6700
    },
    3: {
        "brand": "Seiko",
        "model": "Prospex Turtle",
        "movement": "Automatic",
        "case_material": "Stainless Steel",
        "water_resistance_m": 200,
        "dial_color": "Green",
        "strap_type": "Rubber",
        "price_gbp": 480
    },
    4: {
        "brand": "Casio",
        "model": "G-Shock DW-5600",
        "movement": "Quartz",
        "case_material": "Resin",
        "water_resistance_m": 200,
        "dial_color": "Black",
        "strap_type": "Resin",
        "price_gbp": 85
    },
    5: {
        "brand": "Tag Heuer",
        "model": "Aquaracer",
        "movement": "Automatic",
        "case_material": "Stainless Steel",
        "water_resistance_m": 300,
        "dial_color": "Blue",
        "strap_type": "Bracelet",
        "price_gbp": 2600
    },
    6: {
        "brand": "Tissot",
        "model": "PRX Powermatic 80",
        "movement": "Automatic",
        "case_material": "Stainless Steel",
        "water_resistance_m": 100,
        "dial_color": "Blue",
        "strap_type": "Bracelet",
        "price_gbp": 620
    },
    7: {
        "brand": "Apple",
        "model": "Watch Series 9",
        "movement": "Digital",
        "case_material": "Aluminium",
        "water_resistance_m": 50,
        "dial_color": "Black",
        "strap_type": "Silicone",
        "price_gbp": 399
    },
    8: {
        "brand": "Citizen",
        "model": "Promaster Diver",
        "movement": "Solar",
        "case_material": "Stainless Steel",
        "water_resistance_m": 200,
        "dial_color": "Blue",
        "strap_type": "Rubber",
        "price_gbp": 290
    },
    9: {
        "brand": "Hamilton",
        "model": "Khaki Field Mechanical",
        "movement": "Manual",
        "case_material": "Stainless Steel",
        "water_resistance_m": 50,
        "dial_color": "Black",
        "strap_type": "NATO",
        "price_gbp": 520
    },
    10: {
        "brand": "Longines",
        "model": "HydroConquest",
        "movement": "Automatic",
        "case_material": "Stainless Steel",
        "water_resistance_m": 300,
        "dial_color": "Grey",
        "strap_type": "Bracelet",
        "price_gbp": 1250
    }
}

# print item by id (which doesn't have to be an integer)
print (watches[4])
"""
# show all casios
casio_watches = {
    watch_id: watch
    for watch_id, watch in watches.items()
    if watch["brand"].lower() == "casio"
}

print (casio_watches)

# print out keys
for key in watches:
    print (key)

# Another way which can be slower for large data sets
for watch in watches.values():   
    if watch["brand"].lower() == "casio":
        print (watch)

"""
