class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Hello {self.name}. You are a {self.age} years old {self.gender}")


person1 = Person("Max", 21, "Male")
person1.introduce()
