from validation import validate_mark
from calculations import calculate_total, calculate_average, calculate_grade
from display import display_result


def main():
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        mark = float(input(f"Enter marks for subject {i + 1}: "))

        while not validate_mark(mark):
            print("Invalid marks. Enter 0-100.")
            mark = float(input(f"Enter marks for subject {i + 1}: "))

        marks.append(mark)

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    display_result(name, total, average, grade)


main()