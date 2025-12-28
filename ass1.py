#write a program that asks for three numbers and prints the largest using a function

a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
def large(a,b,c):
    if (a >=b and a >=c):
        return a
    elif (b >=a and b >=c):
        return b
    else:
        return c
large(a,b,c)