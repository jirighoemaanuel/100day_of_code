import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elener"]
students_socres = {student: random.randint(1, 100) for student in names}
print(students_socres)

pass_students = {
    student: score for (student, score) in students_socres.items() if score > 50
}
print(pass_students)
