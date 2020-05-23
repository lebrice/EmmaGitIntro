def foo(a: int, b: int) -> int:
    return a + a ** b + a * b

print("foo(1, 2) = ", foo(1,2))

class Cat:
    def __init__(self, name: str="Bob"):
        self.name = name
        print("Hello! My name is", self.name)

bob = Cat()
charlie = Cat(name="Charlie")
