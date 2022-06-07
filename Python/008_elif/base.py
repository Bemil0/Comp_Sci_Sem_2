x = int(input("Enter your first integer: "))
z = (input("Enter an operation: "))
y = int(input("Enter your second integer: "))
if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "*":
    print(x*y)
elif z == "/":
    print(x/y)
else:
    print("Please enter one of the following for the expression: +, -, *, /")