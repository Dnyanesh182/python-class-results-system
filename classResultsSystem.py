# UC9 – Read Student Results from File

try:
    with open("student_results.txt", "r") as file:
        data = file.read()
        print("Student Results from File:\n")
        print(data)

except FileNotFoundError:
    print("Error: student_results.txt file not found.")