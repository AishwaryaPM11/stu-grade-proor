# app.py
import sys

def calculate_grade(m1, m2, m3):
    avg = (m1 + m2 + m3) / 3

    if avg >= 90: return avg, "S"
    elif avg >= 80: return avg, "A"
    elif avg >= 65: return avg, "B"
    elif avg >= 50: return avg, "C"
    elif avg >= 40: return avg, "D"
    else: return avg, "F"

def main():
    # If arguments are provided
    if len(sys.argv) == 7:
        name = sys.argv[1]
        department = sys.argv[2]
        semester = sys.argv[3]
        m1 = float(sys.argv[4])
        m2 = float(sys.argv[5])
        m3 = float(sys.argv[6])
    else:
        # Default values
        name = "Padmini"
        department = "Bcom"
        semester = "4"
        m1 = 75
        m2 = 80
        m3 = 75

    avg, grade = calculate_grade(m1, m2, m3)

    print("        STUDENT RESULT")
    print("===================")
    print(f"Student Name : {name}")
    print(f"Department   : {department}")
    print(f"Semester     : {semester}")
    print("-----------------------------------")
    print(f"Marks        : {m1}, {m2}, {m3}")
    print(f"Total Marks  : {m1 + m2 + m3}")
    print(f"Average      : {avg:.2f}")
    print(f"Grade        : {grade}")
    print("====================\n")

if __name__ == "__main__":
    main()
