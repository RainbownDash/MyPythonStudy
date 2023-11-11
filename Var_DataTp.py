import math

def myFunc1():

    n1 = int(input("Enter first num: "))
    n2 = int(input("Enter first num: "))
    n3 = int(input("Enter first num: "))
    #Summa
    suma = n1 + n2 + n3
    mult = n1*n2*n3
    power = n1 ** (n2-n3)
    print(suma, mult, power)
#myFunc1()
def myFunc2():
    n = int(input("Enter d: "))
    result = (1 * n) + (11 * n) + (111 * n)
    print(result)

#myFunc2()
def myFunc3():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    hobby = input("Enter your hobby: ")

    print(f"My name is {name}. I am {age} and my hobby is {hobby}.")
#myFunc3()
def PrTriangle():
    baseside = int(input("Введіть значення основи трикутника: "))
    height = int(input("Введіть значення висоти трикутника: "))

    S = float((baseside*height)/2)
    print(f"{S:.2f}") #or "{:.2f}".format(S)
#PrTriangle()
#5
def NextPrevNum():
    mynum = int(input("Enter your number: "))
    print(f"The next number for the number {mynum} is {mynum + 1}\nThe previous number for the number{mynum} is {mynum - 1}")
#NextPrevNum()

def myFunc6():
    n = int(input("Enter num: "))
    print(n % 10)
#myFunc6()
def Circle():
    r = float(input("R = "))
    p = round(math.pi, 2)
    S = p * pow(r, 2)
    C = 2 * p * r
    print(f"{S:.3f}")
    print(f"{C:.3f}")
#Circle()

def mat1():
    a = int(input("a = "))
    b = int(input("b = "))

    print(f"({a} + {b}) * ({b} + {a}) = {(a+b)*(b+a)}")
#at1()

def HightToCm():
    feet = int(input("Feet: "))
    inc = int(input("Inches: "))

    feet *= 30.48
    inc *= 2.54
    Cm = round(feet + inc)
    print(f"Your height is: {Cm} cm.")
HightToCm()