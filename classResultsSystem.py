# UC3 – Store Student Records in List or Dictionary

students = []

for i in range(2):

    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)

print("\nStored Student Records:")
for student in students:
    print(student)