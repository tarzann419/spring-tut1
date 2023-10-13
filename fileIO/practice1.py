students = []

with open("practice1.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {
            "name": name,
            "house": house
        }
        students.append(student)
    for student in sorted(students):
        print(f"{student[name]}")
