import pytest

class FactorialValueFailure(ValueError):
    pass

def factorial(x):
    if x > 950 or x < 1:
        raise FactorialValueFailure
    
    if x == 1:
        return x
    else:
        return x * factorial(x-1)

def test_factorial():
   ### Test 1
   # arrange 
   n = 20
   expected = 2432902008176640000

   # act
   result = factorial(n)

   # assert
   assert result == expected, "Large factorial failed"

   ### Test 2
   # arrange 
   n = 5
   expected = 120

   # act
   result = factorial(n)

   # assert
   assert result == expected, "Conventional factorial failed"

   ### Test 3 ("luxury" example)
   # arrange 
   n = 0
   
   # act
   try:
       result = factorial(n)
       print ("running")
       assert False, "Expected FactorialValueFailure, but didn't get one"
   except FactorialValueFailure:
       pass
   
   # Or you can write it like this:
   with pytest.raises(FactorialValueFailure):
        factorial(n)

