students = [
    {"name": "Ammar", "grades": [88, 90, 83]},
    {"name": "Youssef", "grades": [90, 95, 85]},
    {"name": "Hamza", "grades": [86, 80, 76]}
]

for student in students:
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print("Student:", student["name"], "- Average Grade:", average)
