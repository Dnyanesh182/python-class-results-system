# UC8 – Save Student Results to File

students = [
    {"name": "John", "roll": 101, "marks": [80, 85, 90], "average": 85.0, "grade": "B"},
    {"name": "Alice", "roll": 102, "marks": [92, 88, 95], "average": 91.6, "grade": "A"}
]

with open("student_results.txt", "w") as file:

    for student in students:
        file.write(f"Name: {student['name']}\n")
        file.write(f"Roll Number: {student['roll']}\n")
        file.write(f"Marks: {student['marks']}\n")
        file.write(f"Average: {student['average']}\n")
        file.write(f"Grade: {student['grade']}\n")
        file.write("------------------------\n")

print("Student results saved to file successfully.")