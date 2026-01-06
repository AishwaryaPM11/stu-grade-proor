# app.py
import sys

def calculate_grade(m1, m2, m3):
    avg = (m1 + m2 + m3) / 3

    if avg >= 90:
        grade = "S"
    elif avg >= 80:
        grade = "A"
    elif avg >= 65:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "F"

    return avg, grade


def main():
    if len(sys.argv) == 7:
        name = sys.argv[1]
        department = sys.argv[2]
        semester = sys.argv[3]
        m1 = float(sys.argv[4])
        m2 = float(sys.argv[5])
        m3 = float(sys.argv[6])
    else:
        name = "Padmini"
        department = "BCA"
        semester = "3"
        m1, m2, m3 = 70, 80, 90

    avg, grade = calculate_grade(m1, m2, m3)

    print("\n===================================")
    print("        STUDENT RESULT")
    print("===================================")
    print("Student Name :", name)
    print("Department   :", department)
    print("Semester     :", semester)
    print("-----------------------------------")
    print("Marks        :", m1, m2, m3)
    print("Total Marks  :", m1 + m2 + m3)
    print("Average      :", round(avg, 2))
    print("Grade        :", grade)
    print("===================================\n")


if __name__ == "__main__":
    main()
