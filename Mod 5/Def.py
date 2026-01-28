def printTheReport():
    print ("Printing the report on the screen.")

printTheReport()

#######################
def net(income, outgoings):
    total = income-outgoings
    return total

print (f"You have {net(1000,850)} money left.")
####################### Basic data return, don't use
def netII(income, outgoings): 
   total = income - outgoings 
   print(total) 

jan = netII(1239,578) 
print (jan, type(jan))
#######################

# using *args
def variableArgsOne(*args):
    print (args) # args is a ?

    for arg in args:
        print (arg)

variableArgsOne(10, "Mike Rudolfo", "Tomatoes", 12.00)        

# using **kwargs
def variableArgsTwo(**kwargs):
    print (kwargs) # kwargs is a ?

    for arg, value in kwargs.items():
        print (f"arg name={arg} value={value}")

variableArgsTwo(id= 10, name = "Mike Rudolfo", item="Tomatoes", value=12.00)        

# default args
def mon_spend (spend, salary=2000):
    total = salary - spend
    return total

print (mon_spend(200))

# named arguments - you can specify the parameters in any sequence you think
# is meaningful.  Also useful if combined with default values.
def capital_city (country,city): 
    print(f"The capital city of {country} is {city}.")

capital_city(city = "Madrid", country = "Spain")