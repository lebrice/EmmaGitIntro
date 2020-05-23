def foo(a: int, b: int) -> int:
    return a + a ** b + a * b

print("foo(1, 2) = ", foo(1,2))

class Cat:
    def __init__(self, name: str="Bob"):
        self.name = name
        print("Hello! My name is", self.name)

    def meow(self):
        print(self.name, "says MEOW!")

bob = Cat()
charlie = Cat(name="Charlie")

bob.meow()
charlie.meow()

class Dog:
    def __init__(self, name: str="Bobby"):
        self.name = name
        print("Hello! My name is", self.name)

    def bark(self):
        print(self.name, "says WOOF!")

bobby = Dog()
riley = Dog(name="Riley")

bobby.bark()
riley.bark()
