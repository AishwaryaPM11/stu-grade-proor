import sys

def main():
    # Step 1: Read argument from Jenkins
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Student"

    # Step 2: Fixed values (CI/CD safe)
    department = "CSE"
    semester = 5
    m1, m2, m3 = 70, 80, 90

    avg = (m1 + m2 + m3) / 3

    # Step 3: Grade logic
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

    # Step 4: Output
    print("Name:", name)
    print("Average:", avg)
    print("Grade:", grade)

if __name__ == "__main__":
    main()
