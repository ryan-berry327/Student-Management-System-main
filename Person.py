class Person:

    def __init__(self,name,age,id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID Number: {self.id_number}"
