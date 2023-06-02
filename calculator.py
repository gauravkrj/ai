def calculate(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "Invalid operator"
print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter an operator (+, -, *, /): ")
result = calculate(operation, num1, num2)
print("Result: ", result)

