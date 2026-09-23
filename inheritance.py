class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def show(self):
        print(f"The Employee Id is {self.id} and Name is {self.name}")

class Programmer(Employee):
    def show_language(self):
        print("The language is Python")

e1 = Programmer(1,"dipu")
e1.show()
e1.show_language()
