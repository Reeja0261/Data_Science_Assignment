# print a multiplication tabe for a number , but highlight multiples of 5
a = int(input("enter the number"))

def multiplication(a):
    for i in range(1,11):
        answer = a * i
        if answer % 5 == 0:
            print(f"{a} * {i} = {answer}")
        else:
            print(f"{a} * {i} = {answer}")
multiplication(a)