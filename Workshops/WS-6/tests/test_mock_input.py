# Using monkeypatch to simulate user input (Pytest)
def get_name():
    return input ("Enter your name: ")

def test_get_name(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Alice")
    result = get_name()
    assert result == "Alice"

### Multiple inputs

def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    return {"name": name, "email": email}

def test_add_contact(monkeypatch):
    # an interable allows the receipient to go through each item sequentially, the
    # recipient can then call a next function on each item as it is returned from the list.
    inputs = iter(["Bob", "bob@example.com"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    result = add_contact()
    expected = {"name": "Bob", "email": "bob@example.com"}
    assert result == expected

### Check output
def greet(name):
    print (f"Hello {name}")

def test_greet(monkeypatch):
    printed = []

    def fake_print(msg):
        printed.append (msg)

    monkeypatch.setattr("builtins.print", fake_print)

    greet ("Juniper Bobblesnap")
    
    assert printed[0] == "Hello Juniper Bobblesnap", "Print capture failed"