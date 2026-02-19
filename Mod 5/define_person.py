def process_person(**details):
    for key, value in details.items():
        print (f"{key} is {value}")

process_person(name="Mike", phone="555-3434", age="26")

