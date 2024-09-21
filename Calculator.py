def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."

def calculator():
    print("Welcome to Simple Calculator")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operation = input("Enter your choice (1/2/3/4): ")
    if operation in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the First Number: "))
            num2 = float(input("Enter the Second Number: "))
            if operation == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operation == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operation == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operation == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
