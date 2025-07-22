def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("You cannot divide by zero!")
        return None

operators = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    operand_one = float(input("Enter a number: "))
    operator = input("Choose an operator \n+\n-\n*\n/\n")
    operand_two = float(input("Enter another number: "))
    result = operators[operator](operand_one, operand_two)
    print(f"{operand_one} {operator} {operand_two} = {result}")
    return result

calculating = True

while calculating:
    result = calculator()
    if result == None:
        continue
    continue_calculating = input("Would you like to continue operating on the result? (y/n): ").lower()
    if continue_calculating == "y":
        while continue_calculating == "y":
            new_operator = input("Choose an operator \n+\n-\n*\n/\n")
            new_operand = float(input("Enter a number: "))
            new_result = operators[new_operator](result, new_operand)
            print(f"{result} {new_operator} {new_operand} = {new_result}")
            result = new_result
            continue_calculating = input("Would you like to continue operating on the result? (y/n): ").lower()