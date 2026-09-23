class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)  
print("------------------------------------------")

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def stud_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

stud1 = Student("Dipalee",22,"MCA")
stud2 = Student("Pavitra",19,"12th")

stud1.stud_info()
stud2.stud_info()
