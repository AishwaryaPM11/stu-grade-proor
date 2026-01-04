# app.py

def calculate_grade(m1, m2, m3):
    average = (m1 + m2 + m3) / 3

    if 90 <= average <= 100:
        return average, "S"
    elif 80 <= average <= 89:
        return average, "A"
    elif 65 <= average <= 79:
        return average, "B"
    elif 50 <= average <= 64:
        return average, "C"
    elif 40 <= average <= 49:
        return average, "D"
    else:
        return average, "F"


def main():
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")

    m1 = float(input("Enter Marks for Subject 1: "))
    m2 = float(input("Enter Marks for Subject 2: "))
    m3 = float(input("Enter Marks for Subject 3: "))

    avg, grade = calculate_grade(m1, m2, m3)

    print("\n----- Student Result -----")
    print("Name       :", name)
    print("Department :", department)
    print("Semester   :", semester)
    print("Average    :", round(avg, 2))
    print("Grade      :", grade)


if __name__ == "__main__":
    main()
