
def calculate_total(marks):
    return sum(marks.values())


# Function to calculate percentage
def calculate_percentage(total, subjects):
    return total / subjects


# Function to assign grade
def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


# Function to display result
def display_report(name, marks, total, percentage, grade):

    print("\n------ Student Report ------")
    print("Student Name:", name)

    print("\nMarks:")
    for subject, mark in marks.items():
        print(subject, ":", mark)

    print("\nTotal Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)


# Main Program
try:

    name = input("Enter Student Name: ")

    subjects = int(input("Enter number of subjects: "))

    marks = {}

    for i in range(subjects):

        subject = input("Enter subject name: ")
        mark = int(input("Enter marks: "))

        marks[subject] = mark

    total = calculate_total(marks)

    percentage = calculate_percentage(total, subjects)

    grade = calculate_grade(percentage)

    display_report(name, marks, total, percentage, grade)

except ValueError:
    print("Invalid input! Please enter numbers for marks.")