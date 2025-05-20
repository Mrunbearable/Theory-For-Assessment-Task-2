class Person:
    def __init__(self, full_name, DOB, gender, contacts):
        self.full_name = full_name
        self.DOB = DOB
        self.gender = gender
        self.contacts = contacts

    def display_details(self):
        print(f"Full Name: {self.full_name}, , Dob: {self.dob}, Gender: {self.gender}, Contacts: {self.email}")