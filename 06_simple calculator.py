num1 = int(input("Enter first number: "))
num2 = int(input("Enter  second number : "))

operator = input("Enter operator from +, -, *, /")

match operator:
    case "+":
        print(f"Sum of {num1} and {num2} is ", num1 + num2)
    case "-":
        print(f"Differnce of {num1} and {num2} is ",num1 - num2)
    case "*":
        print(f"Product of {num1} and {num2} is ",num1*num2)
    case "/":
        print(f"Division of {num1} and {num2} is ",num1/num2)
    case _:
        print("Select only from +, -, *, /")

