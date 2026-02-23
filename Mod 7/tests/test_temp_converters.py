import pytest
import utils.temp_converters as tc

@pytest.fixture(scope="module")
def module_setup():   
    print ("Creating pre-initialised test data for all functions in the module to use i.e one test function will collected data"
    "modifications from a previous function.")
    yield
    print ("Module teardown, delete temp files and the like")


@pytest.fixture(scope="function")
def function_setup():   
    print ("Creating pre-initialised test data before running any test function.  " 
    "This can reset any data used every time a test function executes")


def test_FToC(module_setup, function_setup):
    t = 68
    expected = 20

    result = tc.fahrenheit_to_celcius(t)
    assert expected == result, "Temperature conversion from F to C failed"


def test_CToF(module_setup, function_setup):
    t = 20
    expected = 68

    result = tc.celcius_to_fahrenheit(t)
    assert expected == result, "Temperature conversion from C to F failed"

def test_KtoC():
    t = 273.5
    expected = 0

    result = tc.kelvin_to_celcius(t)
    assert expected == result, "Temperature conversion from K to C failed"

# Purposely cause a funnction to fail in a controlled way.  The failure is what you want in order to pass the test.
def test_KtoC_ValueError(module_setup, function_setup):
    t = -1000

    with pytest.raises(ValueError, match="A temperature in Kelvin cannot be below zero.", ):
        tc.kelvin_to_celcius(t)


