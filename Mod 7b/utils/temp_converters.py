def CtoF(temp):
    return (temp * 9 / 5) + 32

def FtoC(temp):
    return (temp - 32) * (5 / 9)

def CtoK(temp):
    return temp + 273.5

def KtoC(temp):
    if temp < 0:
        raise ValueError("A temperature in Kelvin cannot be below zero.")
    
    return temp - 273.5

def FtoK(temp):
    return FtoC(temp) + 273.5

def KtoF(temp):
    if temp < 0:
        raise ValueError("A temperature in Kelvin cannot be below zero.")
    
    return CtoF(temp - 273.5)

