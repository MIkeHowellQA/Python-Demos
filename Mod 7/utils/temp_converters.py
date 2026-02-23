def celcius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32

def fahrenheit_to_celcius(temp):
    return (temp - 32) * (5 / 9)

def celcius_to_kelvin(temp):
    return temp + 273.5

def kelvin_to_celcius(temp):
    if temp < 0:
        raise ValueError("A temperature in Kelvin cannot be below zero.")
    
    return temp - 273.5

def fahrenheit_to_kelvin(temp):
    return fahrenheit_to_celcius(temp) + 273.5

def kelvin_to_fahrenheit(temp):
    if temp < 0:
        raise ValueError("A temperature in Kelvin cannot be below zero.")
    
    return celcius_to_fahrenheit(temp - 273.5)

