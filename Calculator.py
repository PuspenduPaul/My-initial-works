def add(x,y):
    return x + y
def substract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def exponential(x,y):
    return x ** y
def Modulus(x,y):
    return x % y
def floor_division(x,y):
    return x // y

print('1.Add ')
print('2.Substract ')
print('3.Multiply ')
print('4.Divide ')
print('5.Exponential ')
print('6.Modulus ')
print('7.Floor Divide ')

choice = float(input("Choose an option(1/2/3/4/5/6/7): "))

print('I')
print('I')
print('I')

num_1 = float(input('Give the first number: '))
num_2 = float(input('Give the second number: '))

if choice == 1:
    print(num_1, "+", num_2, "=",add(num_1,num_2) )
elif choice == 2:
    print(num_1, "-", num_2, "=", substract(num_1, num_2))
elif choice == 3:
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 4:
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
elif choice == 5:
    print(num_1, "**", num_2, "=", exponential(num_1, num_2))
elif choice == 6:
    print(num_1, "%", num_2, "=", Modulus(num_1, num_2))
elif choice == 7:
    print(num_1, "//", num_2, "=", floor_division(num_1, num_2))
else:
    print('Syntax Error ')
