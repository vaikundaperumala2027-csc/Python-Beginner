num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, //, %): ")
num2 = float(input("Enter the second number: "))
if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Division by zero is not allowed!")
elif operator == "//":
    if num2 != 0:
        print("Result =", num1 // num2)
    else:
        print("Error: Division by zero is not allowed!")
elif operator == "%":
    if num2 != 0:
        print("Result =", num1 % num2)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Error: Invalid operator!")