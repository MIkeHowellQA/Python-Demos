import unittest

def add(a, b):
    return a - b

class TestAdd(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(2,3), 5)

# The IF statement below checks if you are either running this file or importing it as a module.
# If you type in 
#    python demo_unittest.py 
# it will run unittest.main, triggering the unit test engine.
#
# If you import this file as a module, the unittest.main() won't run, but the functions will be available to 
# the importer.

if __name__ == "__main__":
    unittest.main()

