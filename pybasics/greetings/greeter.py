class Greeter:
    def __init__(self, name: str):
        #like constructor
        self.name = name

    def say_hello(self) -> str:
        #instance method
        return f"Hello, {self.name}!"