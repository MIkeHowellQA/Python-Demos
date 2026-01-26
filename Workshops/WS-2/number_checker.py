n = float(input ("Give me a number you dirty dog you...:"))

if n > 0:
    print ("Your number is positive, a ray of sunshine!")
elif n < 0:
    print ("Your number is negative, so sad, but just for now.")
else:
    print ("Well that's a rather dull neutral number.")

if n == int(n):
    # if n % 2 == 0:
    if int(n) & 1:
        print ("Your number is even and steady, like an ancient sequoia tree in a forest.")
    else:
        print ("Your number is odd, just like you.")
else:
    print ("Your number can't be checked for oddity or evenity, for it floats amongst the waves.")

