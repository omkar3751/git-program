# To create calculator using User input & choose the operator.

first = float(input("Enter first number:"))
operator = input("Enter Operator (+,-,*,/,%):")
second = float(input("Enter second number:"))

if operator=="+":
    print(first + second)
elif operator=="-":
    print(first - second)
elif operator=="*":
    print(first * second)
elif operator=="/":
    print(first / second)
elif operator=="%":
    print(first % second)

else:
    print("operator Invalid:")
    
    
