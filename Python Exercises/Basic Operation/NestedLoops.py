# Given the names and grades for each student in a Physics class of Nstudents, store them in a nested list and print the
# name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a
# new line.

"""
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""


def second_smallest(numbers):
    m2 = float('inf')
    m1 = min(numbers)

    for j in numbers:
        if j > m1:
            if j < m2:
                m2 = j

    return m2

if __name__ == '__main__':

    names = list()
    scores = list()
    student_number = int(input())

    for _ in range(student_number):
        names.append(input())
        scores.append(float(input()))

    num = second_smallest(scores)

    print_names = list()

    for index in range(student_number):
        if scores[index] == num:
            print_names.append(names[index])

    print_names.sort()

    for n in print_names:
        print(n)
