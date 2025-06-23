# List of students with their marks
students = [
    {"name": "Arya", "marks": 95},
    {"name": "John", "marks": 82},
    {"name": "Mira", "marks": 91},
    {"name": "Kabir", "marks": 78},
    {"name": "Sana", "marks": 97}
]

# Define ranker criteria (above 90)
rankers = []

# Linear Search to find rankers
for student in students:
    if student["marks"] > 90:
        rankers.append(student["name"])

# Output
if rankers:
    print("Rankers (above 90 marks):")
    for name in rankers:
        print("-", name)
else:
    print("No rankers found.")
