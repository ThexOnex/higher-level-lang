# object orirented Programing
# primited data type:
# byte int float double char boolean
# structure ==> position/feel/color
# object : instance of class
# class: template for the object
# class Dog:...
# d = Dog()    # d is object of type Dog
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


d = Dog("Tim", 18)
print(d.get_name())
d2 = Dog("Bill", 20)
print(d2.get_name())
