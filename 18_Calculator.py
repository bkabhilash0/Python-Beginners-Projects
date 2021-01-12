# A very basic command line Calculator.
class Calculator:
    def __init__(self):
        pass
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        return x//y
    def modulus(self,x,y):
        return x%y

def calcu(x):
    try:
        print(f"The answer for the expression {x} is equal to {eval(x)}")
    except :
        print("Enter a Valid Mathematical Expression!")

n = input("Enter the expression:\n>> ")
calcu(n)
calc = Calculator()
sum = calc.add(5,6)
print(sum)
