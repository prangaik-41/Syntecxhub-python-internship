"""project 1 is of making Simple calculator which 
 takes inputs of numbres and operator and calculate according to it """

#here we use function for performing different for diffrent operator
def calculator():
    print("----SIMPLE CALCULATOR----")
    print("First Number")
    #taking first number in input and store in a
    a = float(input("Enter First Number: "))
    print("Second Number")
    #taking Second number in input and store in b
    b = float(input("Enter Second Number: "))
    print("Choose Operator")
    #choose operators from +,-,*,/  as input and stire in operatt
    operator = input("Choose Operation(+,-,*,/): ")
    if operator == "+":
        print("--Addition--")
        print(f"{a} + {b} =", a+b)
    elif operator == "-":
        print("--Substarction--")
        print(f"{a} - {b} =",a-b)
    elif operator == "*":
        print("--multiplication--")
        print(f"{a} * {b} =",a*b)
    elif operator == "/":
        print("--Division--")
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print(f"{a} / {b} =",a / b)
    else:
        print("Enter correct operator(+,-,*,/)")
calculator()

