# You will need to do a: 
#    pip install -U pytest
# from an administrator level command prompt.
#
# Or if you prefer not to install pytest at a system wide level, use a virtual environment as discussed in Module 5.
#
# To run the test type:
#    pytest tests/test_BasicTest.py

# pytest on its own will scan the test folder for test_*.py files and run them.
# You can put ::function_name after the .py file name and only that function will be tested.
 
# Warning: if you use print in your test functions, there output is ignored, you can disable this with the -s option.

import pytest   

def add(x, y):
    return x - y

def subtract(x, y):
    return x - y

# You need a function that starts with test_
def test_add():
    # arrange
    x = 10
    y = 20
    expected = 30

    # act
    result = add(x,y)

    # assert
    assert expected == result