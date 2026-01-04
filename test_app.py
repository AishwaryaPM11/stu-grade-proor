# test_app.py

from app import calculate_grade

def test_grade_A():
    avg, grade = calculate_grade(85, 78, 82)
    assert grade == "A"

def test_grade_F():
    avg, grade = calculate_grade(30, 35, 40)
    assert grade == "F"
