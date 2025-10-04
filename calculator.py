def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    print("-----Calculator-----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter a choice: ")

    if choice in ["1", "2", "3", "4", "5"]:

        if choice == "5":
            print("Exiting calculator...")
            break

        num1 = get_input("Enter first number: ")
        num2 = get_input("Enter second number: ")

        if choice == "1":
            print("Result: ", add(num1, num2))
        elif choice == "2":
            print("Result: ", subtract(num1, num2))
        elif choice == "3":
            print("Result: ", multiply(num1, num2))
        elif choice == "4":
            print("Result: ", divide(num1, num2))
        
    else:
        print("Invalid input!")