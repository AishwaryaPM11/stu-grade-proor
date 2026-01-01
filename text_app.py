from app import calculate_grade

def test_grade_s():
    assert calculate_grade(95) == "S"

def test_grade_a():
    assert calculate_grade(85) == "A"

def test_grade_b():
    assert calculate_grade(70) == "B"

def test_grade_c():
    assert calculate_grade(55) == "C"

def test_grade_d():
    assert calculate_grade(45) == "D"

def test_grade_f():
    assert calculate_grade(30) == "F"
