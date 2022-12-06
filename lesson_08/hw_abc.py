from abc import ABC, abstractmethod
from random import choice


class Shape(ABC):
    @staticmethod
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    """Changed"""

    def draw(self):
        print(" ----")
        print(" |  |")
        print(" ----")


class Circle(Shape):
    """Changed"""

    def draw(self):
        print(" --")
        print("-  -")
        print(" --")


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle
    """
    circle = Circle()
    rectangle = Rectangle()
    options: list[Shape] = [circle, rectangle]
    return choice(options)


def main():
    """
    In Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
