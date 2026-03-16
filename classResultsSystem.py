# UC2 – Add Student Details (Name, Roll Number, Marks)

students = []

name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

student = {
    "name": name,
    "roll": roll,
    "marks": marks
}

students.append(student)

print("\nStudent added successfully.")
print("Current Student Records:")
for s in students:
    print(s)