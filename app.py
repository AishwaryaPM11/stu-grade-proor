# app.py
import sys

def calculate_grade(m1, m2, m3):
    avg = (m1 + m2 + m3) / 3
    if 90 <= avg <= 100: return avg, "S"
    elif 80 <= avg <= 89: return avg, "A"
    elif 65 <= avg <= 79: return avg, "B"
    elif 50 <= avg <= 64: return avg, "C"
    elif 40 <= avg <= 49: return avg, "D"
    else: return avg, "F"

def main():
    # Check if all arguments are provided
    if len(sys.argv) != 7:
        print("Usage: python app.py <Name> <Department> <Semester> <Mark1> <Mark2> <Mark3>")
        sys.exit(1)

    name = sys.argv[1]
    department = sys.argv[2]
    semester = sys.argv[3]
    m1 = float(sys.argv[4])
    m2 = float(sys.argv[5])
    m3 = float(sys.argv[6])

    avg, grade = calculate_grade(m1, m2, m3)

    print("\n----- Student Result -----")
    print("Name       :", name)
    print("Department :", department)
    print("Semester   :", semester)
    print("Average    :", round(avg, 2))
    print("Grade      :", grade)

if __name__ == "__main__":
    main()
