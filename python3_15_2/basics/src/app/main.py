from app.greetings.greeter import Greeter


def run() -> None:
    greeter = Greeter("World")
    print(greeter.say_hello())
