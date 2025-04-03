expression = input("Enter an expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)
if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    if z == 0:
        print("Error: Division by zero")
    else:
        print(float(x / z))
else:
    print("Error: Invalid operator")