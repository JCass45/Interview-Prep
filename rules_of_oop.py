class Person:
    '''
    Encapsulation
    '''

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender

    def setName(self, new_name):
        self.__name = new_name

    def setAge(self, new_age):
        self.__age = new_age

    # lol
    def setGender(self, new_gender):
        self.__gender = new_gender


class Animal:
    '''
    Inheritance and Polymorphism
    '''

    def make_sound(self):
        print('Animal sound')

    def make_another_sound(self):
        print('Another Animal sound')


class Dog(Animal):
    '''
    Inheritance and Polymorphism
    '''

    def make_sound(self):
        print('Woof')


if __name__ == '__main__':
    animal = Animal()
    dog = Dog()
    animal.make_sound()
    animal.make_another_sound()
    dog.make_sound()
    dog.make_another_sound()
