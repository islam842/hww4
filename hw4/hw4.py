class Person:
    def _init_(self):
        self.name = "Islam"

    def get_name(self):
        return self.name


class Animal:
    def _init_(self):
        self.age = 0

    def get_age(self):
        return self.age


class Car:
    def drive(self):
        print("Car is driving.")


class Employee(Person):
    def _init_(self):
        super()._init_()
        self.salary = 5000

    def get_salary(self):
        return self.salary


class Dog(Animal):
    def _init_(self):
        super()._init_()
        self.breed = "Unknown"

    def get_breed(self):
        return self.breed


class SuperClass(Employee, Dog, Car, Animal, Person):
    def _init_(self):
        super()._init_()
        self.name = "Islam"
        self.age = 15

    def print_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Breed:", self.breed)

    def bark(self):
        print("Woof!")


file = open('command.txt', 'w', encoding='UTF-8')
file.write('git commit -m ' ''
           '\ngit remote add origin link'
           '\ngit checkout name branch'
           '\ngit init'
           '\ngit push origin name to branch'
           '\ngit remote remove origin'
           '\ngit rm --cached name to file'
           '\ngit rm --cached -r name to dir'
           '\ngit branch\ngit branch name to branch'
           '\ngit add .'
           '\ngit branch -d name to branch '
           '\ngit checkout -b name to branch'
           '\ngit merge name to branch')
file.close()
