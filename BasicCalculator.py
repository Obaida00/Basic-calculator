print("Hello and welcome to the basic calculater by OBAIDA ALMELHEM")

num1 = float(input('Enter first number\n'))
num2 = float(input('Enter second number\n'))

oper = input("select an operator:\n [ x , / , + , - ]\n")
print("Result: ", end='')
if oper == 'x':
    print(num1 * num2)
elif oper == '/':
    print(num1 / num2)
elif oper == '+':
    print(num1 + num2)
elif oper == '-':
    print(num1 - num2)
else:
    print('INVALID OPERATOR!!\n Please Try Again..')
    # put all of it inside a function and call it from here
