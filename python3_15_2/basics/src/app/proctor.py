def run() -> None:
    print("Hello from proctor!")
    numbers = [1, 2, 3, 4, 5]
    coords = (1, 2, 3, 4, 5)
    words = {"one": 1, "two": 2, "three": 3}

    print(f"List: {numbers}")
    print(f"Tuple: {coords}")
    print(f"Dictionary: {words}")

    numbers.append(6)
    coords += (6,)
    words["four"] = 4

    print(f"Updated List: {numbers}")
    print(f"Updated Tuple: {coords}")
    print(f"Updated Dictionary: {words}")


if __name__ == "__main__":
    run()

