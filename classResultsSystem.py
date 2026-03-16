# UC7 – Display Individual Student Result

students = [
    {"name": "John", "roll": 101, "marks": [80, 85, 90], "average": 85.0, "grade": "B"},
    {"name": "Alice", "roll": 102, "marks": [92, 88, 95], "average": 91.6, "grade": "A"}
]

roll_number = int(input("Enter roll number to view result: "))

found = False

for student in students:
    if student["roll"] == roll_number:
        print("\nStudent Result")
        print("Name:", student["name"])
        print("Roll Number:", student["roll"])
        print("Marks:", student["marks"])
        print("Average:", student["average"])
        print("Grade:", student["grade"])
        found = True
        break

if not found:
    print("Student record not found.")