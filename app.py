import sys

def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Student"

    m1, m2, m3 = 70, 80, 90
    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    print("Name:", name)
    print("Average:", avg)
    print("Grade:", grade)

if __name__ == "__main__":
    main()
