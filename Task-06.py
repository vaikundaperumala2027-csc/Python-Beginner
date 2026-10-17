def calculate_grade(mark):
    if mark < 0 or mark > 100:
        return "Invalid marks! Enter marks between 0 and 100."
    elif mark >= 90:
        return "Grade A"
    elif mark >= 75:
        return "Grade B"
    elif mark >= 60:
        return "Grade C"
    elif mark >= 50:
        return "Grade D"
    else:
        return "Grade F"
mark = int(input("Enter your mark: "))
grade = calculate_grade(mark)
print("Your Grade:", grade)
