from unittest import TestCase
from unittest.mock import patch

def get_name():
    return input ("Enter your name: ")

class TestInput(TestCase):
    @patch("builtins.input", return_value="Alice")

    def test_get_name(self, mock_input):
        self.assertEqual (get_name(), "Alice")

### Multiple inputs

def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    return {"name": name, "email": email}

@patch("builtins.input", side_effect=["Bob", "bob@example.com"])
def test_add_contact(mock_input):
    result = add_contact()
    expected = {"name": "Bob", "email": "bob@example.com"}
    assert result==expected
