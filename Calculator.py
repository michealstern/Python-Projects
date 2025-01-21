# Function to perform arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

while True:
    # Main program
    def calculator():
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        # Get user input for operation choice
        choice = float(input("\nEnter choice (1/2/3/4): "))

        # Get user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"{num1} + {num2} = {add(num1, num2)}\n")
            elif choice == 2:
                print(f"{num1} - {num2} = {subtract(num1, num2)}\n")
            elif choice == 3:
                print(f"{num1} * {num2} = {multiply(num1, num2)}\n")
            elif choice == 4:
                print(f"{num1} / {num2} = {divide(num1, num2)}\n")
            else:
                print("Invalid input! Please select a valid operation.")
        except ValueError:
            print("Invalid number! Please enter numeric values.")

    # Run the calculator
    calculator()
    repeat = input("Do you want to stop the program: (yes/no) ")
    if repeat == "yes" or repeat == "YES" or repeat == "Yes":
        break
