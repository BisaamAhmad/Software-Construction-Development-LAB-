#Employee name, Basic Salary, Allowance, Tax rate
#calculate_gross_salary(), calculate_tax(), calculate_net_salary()

def employee_input():
    name = input("Enter your name: ")
    basicsalary = float(input("Enter your basic salary: "))
    allowance = float(input("Enter your allowance: "))
    taxrate = float(input("Enter your tax rate: "))
    return name, basicsalary, allowance, taxrate

employee_name, basic_salary, allowance, tax_rate = employee_input()

def calculate_gross_salary(basic_salary, allowance):
    gross_salary = basic_salary + allowance
    return gross_salary

def calculate_tax(gross_salary, taxrate):
    tax = gross_salary * (taxrate / 100)
    return tax

def calculate_net_salary(gross_salary, tax):
    net_salary = gross_salary - tax
    return net_salary

gross_salary = calculate_gross_salary(basic_salary, allowance)
tax = calculate_tax(gross_salary, tax_rate)
net_salary = calculate_net_salary(gross_salary, tax)

with open('employee_salary_calculator.txt', 'a') as file:
    file.write(f"{employee_name}, {basic_salary}, {allowance}, {tax_rate}, {tax}, {net_salary}\n")


print("\n==========Employee Salary Calculator==========")
print("Employee Name = ", employee_name)
print("Basic Salary = ", basic_salary)
print("Allowance = ", allowance)
print("Tax Rate = ", tax_rate, "%")
print("Tax = ", tax)
print("Net Salary = ", net_salary)
print("================================================")