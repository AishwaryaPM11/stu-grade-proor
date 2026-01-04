# student_grade.py

name = input("Enter Student Name: ")
department = input("Enter Department: ")
semester = input("Enter Semester: ")

m1 = float(input("Enter Marks for Subject 1: "))
m2 = float(input("Enter Marks for Subject 2: "))
m3 = float(input("Enter Marks for Subject 3: "))

average = (m1 + m2 + m3) / 3

if 90 <= average <= 100:
    grade = "S"
elif 80 <= average <= 89:
    grade = "A"
elif 65 <= average <= 79:
    grade = "B"
elif 50 <= average <= 64:
    grade = "C"
elif 40 <= average <= 49:
    grade = "D"
else:
    grade = "F"

print("\n----- Student Result -----")
print("Name       :", name)
print("Department :", department)
print("Semester   :", semester)
print("Average    :", round(average, 2))
print("Grade      :", grade)
