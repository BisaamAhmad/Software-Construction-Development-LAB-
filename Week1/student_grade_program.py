def std_input():
    name = input("Enter your name: ")
    subject_num = int(input("How many subjects do you have? "))
    marks = []
    for i in range(subject_num):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        if mark > 0:
            marks.append(mark)
        else:
            print("Please enter a positive number.")
            marks.append(0)
    return name, marks

std_name, std_marks = std_input()

def process_student(std_name, std_marks):
    total = sum(std_marks)
    average = total / len(std_marks)

    if average >= 80:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    else:
        grade = 'F'

    with open('result.txt', 'a') as file:
        file.write(f"{std_name}, {grade}\n")

    return grade

std_grade = process_student(std_name,std_marks)
def print_std_grade(std_name, std_marks, std_grade):
    print('Student Name:', std_name)
    print('Student Marks:', std_marks)
    print('Student Grade:', std_grade)

print_std_grade(std_name, std_marks, std_grade)
