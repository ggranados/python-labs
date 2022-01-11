# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def _sum(n1, n2):
    return int(n1) + int(n2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a = input("Enter the first number:")
    b = input("Enter the second number:")
    c = _sum(a, b)
    print("The sum is:" + str(c))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
