basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
deductions = float(input("Enter deductions: "))
if basic < 0 or allowances < 0 or deductions < 0:
    print("Error: Negative values are not allowed!")
else:
    gross_salary = basic + allowances
    if deductions > gross_salary:
        print("Error: Deductions cannot exceed gross salary.")
    else:
        net_salary = gross_salary - deductions
        if gross_salary > 0:
            percentage = (deductions / gross_salary) * 100
        else:
            percentage = 0
        print("Gross Salary =", gross_salary)
        print("Net Salary =", net_salary)
        print("Deduction Percentage =", round(percentage, 2), "%")