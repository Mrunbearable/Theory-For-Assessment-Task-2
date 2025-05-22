class Person:
    def __init__(self, full_name, DOB, gender, contacts):
        self.full_name = full_name
        self.DOB = DOB
        self.gender = gender
        self.contacts = contacts

    def display_details(self):
        print(f"Full Name: {self.full_name}, , Dob: {self.DOB}, Gender: {self.gender}, Contacts: {self.contacts}")

class Parent(Person):
    def __init__(self, full_name, DOB, gender, contacts, job, address):
        super().__init__(full_name, DOB, gender, contacts)
        self.job = job
        self.address = address

    def get_stats(self):
        print(f"Name: {self.full_name}")
        print(f"Date Of Birth: {self.DOB}")
        print(f"Gender: {self.gender}")
        print(f"Contacts: {self.contacts}")
        print(f"Job: {self.job}")
        print(f"Address: {self.address}")

class Teacher(Person):
    def __init__(self, full_name, DOB, gender, contacts, subject, address):
        super().__init__(full_name, DOB, gender, contacts)
        self.subject = subject
        self.address = address

    def get_stats(self):
        print(f"Name: {self.full_name}")
        print(f"Date Of Birth: {self.DOB}")
        print(f"Gender: {self.gender}")
        print(f"Contacts: {self.contacts}")
        print(f"Subjects: {self.subject}")
        print(f"Address: {self.address}")

class Student(Person):
    def __init__(self, full_name, DOB, gender, contacts, year):
        super().__init__(full_name, DOB, gender, contacts)
        self.year = year
    
    def get_stats(self):
        print(f"Name: {self.full_name}")
        print(f"Date Of Birth: {self.DOB}")
        print(f"Gender: {self.gender}")
        print(f"Contacts: {self.contacts}")
        print(f"Year: {self.year}")


parent = Parent("Ellen", 14/11/1987, "Male", "Ellen@gmail.com", "Chemical Engineer", "Gosford")
teacher = Teacher("Jonas", 27/11/1986, "Female", "Jonas2786@gmail.com", "Science, Mathematics", "Gosford")
student = Student("Krisitine", 30/12/2005, "FeMale", "Krisitine@education.nsw.gov.au", 10)

parent.get_stats()
teacher.get_stats()
student.get_stats()

