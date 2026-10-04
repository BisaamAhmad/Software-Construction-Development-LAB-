def display_result(name, total, average, grade):
    print("\nStudent Result")
    print("----------------")
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)

    with open('result.txt', 'a') as file:
        file.write(f"{name, total, average, grade},\n")