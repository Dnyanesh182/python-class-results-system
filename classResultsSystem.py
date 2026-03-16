# UC10 – Display Complete Class Result Summary

students = [
    {"name": "John", "roll": 101, "average": 85.0, "grade": "B"},
    {"name": "Alice", "roll": 102, "average": 91.6, "grade": "A"},
    {"name": "Bob", "roll": 103, "average": 72.5, "grade": "C"}
]

print("\n------ Class Result Summary ------")

total_students = len(students)
total_average = 0

for student in students:
    print("Name:", student["name"])
    print("Roll Number:", student["roll"])
    print("Average:", student["average"])
    print("Grade:", student["grade"])
    print("-----------------------------")

    total_average += student["average"]

class_average = total_average / total_students

print("Total Students:", total_students)
print("Class Average Marks:", class_average)
print("-----------------------------------")