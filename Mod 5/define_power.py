def power(b, e):
    if e == 1:
        return b
    else:
        return b * power(b,e -1)
    
print (f"2^5 is {power(2,5)}")