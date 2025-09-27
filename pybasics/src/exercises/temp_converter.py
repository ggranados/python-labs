# Temperature Converter
# Write a program that asks the user for a temperature in Celsius and prints it in Fahrenheit.
# (Formula: F = C * 9/5 + 32)
N_DIGITS = 2


def main():
    celsius = float(input("Introduce la temperatura en Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C son {fahrenheit}°F")
    print(f"{fahrenheit}°F son {fahrenheit_to_celsius(fahrenheit)}")


def celsius_to_fahrenheit(celsius)-> float:
    return round((celsius * 9/5) + 32, N_DIGITS)


def fahrenheit_to_celsius(fahrenheit) -> float:
    return round((fahrenheit - 32) * 5 / 9, N_DIGITS)


main()