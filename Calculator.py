class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        return x + y

    def substract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def exponential(self, x, y):
        return x ** y

    def Modulus(self, x, y):
        return x % y

    def floor_division(self, x, y):
        return x // y


print("1. Add ",
      "2. Substract ",
      "3. Multiply ",
      "4. Divide ",
      "5. Exponent ",
      "6. Modulus ",
      "7. Floor division ")
choice = int(input("Give a value: "))

num = Calculator(float(input()), float(input()))
if choice == 1:
    print(f"{num.x} + {num.y} = {num.add(num.x, num.y)}")
elif choice == 2:
    print(f"{num.x} - {num.y} = {num.substract(num.x, num.y)}")
elif choice == 3:
    print(f"{num.x} * {num.y} = {num.multiply(num.x, num.y)}")
elif choice == 4:
    print(f"{num.x} / {num.y} = {num.divide(num.x, num.y)}")
elif choice == 5:
    print(f"{num.x} ** {num.y} = {num.exponential(num.x, num.y)}")
elif choice == 6:
    print(f"{num.x} % {num.y} = {num.Modulus(num.x, num.y)}")
elif choice == 7:
    print(f"{num.x} // {num.y} = {num.floor_division(num.x, num.y)}")
else:
    print("Syntax error")
