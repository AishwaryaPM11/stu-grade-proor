def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg <= 89:
        return "A"
    elif 65 <= avg <= 79:
        return "B"
    elif 50 <= avg <= 64:
        return "C"
    elif 40 <= avg <= 49:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")

    m1 = float(input("Enter Marks 1: "))
    m2 = float(input("Enter Marks 2: "))
    m3 = float(input("Enter Marks 3: "))

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    print("\n--- Student Result ---")
    print(f"Name: {name}")
    print(f"Department: {department}")
    print(f"Semester: {semester}")
    print(f"Average Marks: {avg:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
