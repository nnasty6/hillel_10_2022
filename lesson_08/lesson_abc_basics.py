from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def say_hallo(self):
        raise NotImplementedError


class Dog(Animal):
    def say_hallo(self):
        print("I am dog")


class Cat(Animal):
    def say_hallo(self):
        print("I am cat")


jack = Dog()
jack.say_hallo()

tom = Cat()
tom.say_hallo()
