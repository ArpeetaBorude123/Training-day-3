def add(a, b):
    print("Result =", a + b)

def sub(a, b):
    print("Result =", a - b)

def multiple(a, b):
    print("Result =", a * b)

def div(a, b):
    print("Result =", a / b)


while True:
    print("\n1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you!")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        add(a, b)

    elif choice == 2:
        sub(a, b)

    elif choice == 3:
        multiple(a, b)

    elif choice == 4:
        if b != 0:
            div(a, b)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid choice")