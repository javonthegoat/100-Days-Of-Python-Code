def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operators = {"+": add, "-": subtract, "*": multiply, "/": divide}

operand_one = float(input("Enter a number: "))
operator = input("Choose an operator \n+\n-\n*\n/\n")
operand_two = float(input("Enter another number: "))
operation = operators[operator](operand_one, operand_two)

print(f"{operand_one} {operator} {operand_two} = {operation}")