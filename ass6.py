# build a simple grade calculator for multiple students. input their marks in a list and print the grade using a function.
def grade(marks):
    avg = sum(marks) / len(marks)

    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

num = int(input("How many students? "))

for i in range(num):
    print("Student", i + 1)
    marks = list(map(int, input("Enter marks: ").split()))
    print("Grade =", grade(marks))