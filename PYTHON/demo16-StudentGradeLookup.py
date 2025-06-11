student_grades = {
    'Alice': 85,
    'Bob': 90
}

query_name = input("Enter the student's name: ")

if query_name in student_grades:
    print(f"{query_name}'s grade is {student_grades[query_name]}")
else:
    print(f"{query_name} is not found in the records")
