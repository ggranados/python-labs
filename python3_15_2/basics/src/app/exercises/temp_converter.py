N_DIGITS = 2


def celsius_to_fahrenheit(celsius: float) -> float:
    return round((celsius * 9 / 5) + 32, N_DIGITS)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return round((fahrenheit - 32) * 5 / 9, N_DIGITS)


def run() -> None:
    celsius = float(input("Introduce la temperatura en Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C son {fahrenheit}°F")
    print(f"{fahrenheit}°F son {fahrenheit_to_celsius(fahrenheit)}°C")
