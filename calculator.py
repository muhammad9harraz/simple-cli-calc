def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "\nError: Division by zero!"
    return x / y

def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nInvalid input! Please enter a number.")

while True:
    print("\n-----Calculator-----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter a choice: ")

    if choice in ["1", "2", "3", "4", "5"]:

        if choice == "5":
            print("\nExiting calculator...")
            break

        num1 = get_input("\nEnter first number: ")
        num2 = get_input("\nEnter second number: ")

        if choice == "1":
            print("\nResult: ", add(num1, num2))
        elif choice == "2":
            print("\nResult: ", subtract(num1, num2))
        elif choice == "3":
            print("\nResult: ", multiply(num1, num2))
        elif choice == "4":
            print("\nResult: ", divide(num1, num2))
        
    else:
        print("\nInvalid input!")