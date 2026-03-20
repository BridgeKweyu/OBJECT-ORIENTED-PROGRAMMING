class Student:
    def __init__(self, name, age):
        self.name = name      
        self.age = age        

    def introduce(self):      
        print(f"My name is {self.name} and I am {self.age} years old.")

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(student1.name)

student1.introduce()
student2.introduce()