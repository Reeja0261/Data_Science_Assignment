# write a program that asks for 5 numbers and print the largest number

def largest(arr_):   #underscore gara variable bhayo
    max_number = arr_[0]
    for a in arr_[1:]:
        if a > max_number:
            max_number = a
        return max_number
largest([-1,-2,-7,-5,-5])