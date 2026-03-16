# UC4 – Calculate Total Marks for Each Student

students = []

for i in range(2):

    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))

    marks1 = float(input("Enter marks for Subject 1: "))
    marks2 = float(input("Enter marks for Subject 2: "))
    marks3 = float(input("Enter marks for Subject 3: "))

    total = marks1 + marks2 + marks3

    student = {
        "name": name,
        "roll": roll,
        "marks": [marks1, marks2, marks3],
        "total": total
    }

    students.append(student)

print("\nStudent Total Marks:")
for student in students:
    print(student["name"], "Total Marks:", student["total"])