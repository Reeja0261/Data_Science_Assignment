# roll a dice 10 times using random.randit() and count how many times you get it.
import random

def dice():
    count = 0
    for i in range(10):
        r = random.randint(1, 6)
        print("Roll:", r)
        if r == 6:
            count += 1
    return count

print(dice())