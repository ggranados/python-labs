class Greeter:
    def __init__(self, name: str):
        self.name = name

    def say_hello(self) -> str:
        return f"Hello, {self.name}!"


def run() -> None:
    greeter = Greeter("World")
    print(greeter.say_hello())
