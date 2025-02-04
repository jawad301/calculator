first = int(input("Enter the first value"))
second = int(input(" Enter the second value"))
oper = str(input("Enter operation +, -, *, /"))

if oper == "+":
    print(first + second)
elif oper == "-":
    print(first - second)
elif oper == "*":
    print(first * second)
elif oper == "/":
    print(first / second)
else:
    print("Invalid operation")