is_active = False
months = 0
performance_rating = 0
discipline_action = False
attendance = 0
def input_data():
    is_active = input("Enter true or false: ").lower() == "true"
    months = int(input("Enter number of months: "))
    performance_rating = float(input("Enter your performance: "))
    discipline_action = input("Enter true or false: ").lower() == "true"
    attendance = float(input("Enter your attendance: "))

    return is_active, months, performance_rating, discipline_action, attendance
is_active, months, performance_rating, discipline_action, attendance = input_data()

def employee_bonus_eligibility(is_active, months, performance_rating, discipline_action, attendance):
    if is_active == True:
        if months >= 12 and performance_rating >= 4 and discipline_action == False and attendance >= 90:
            print("\nEmployee Bonus Eligibility")
            print(
                "Is Active =", is_active,
                "Months =", months,
                "Performance Rating =", performance_rating,
                "Discipline Action =", discipline_action,
                "Attendance =", attendance
            )
            return True
        else:
            print("\nEmployee is Active but NOT eligible for bonus.")
            return False
    else:
        print("\nUser not Found")
        return False

result = employee_bonus_eligibility(is_active, months, performance_rating, discipline_action,attendance)

print("\nEmployee Information")
print(
    "Is Active =", is_active,
    "Months =", months,
    "Performance Rating =", performance_rating,
    "Discipline Action =", discipline_action,
    "Attendance =", attendance
)
print("Bonus Eligible =", result)