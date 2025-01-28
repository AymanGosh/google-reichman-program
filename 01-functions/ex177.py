def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


assert letter_grade(100) == "A"
assert letter_grade(95) == "A"
assert letter_grade(90) == "A"
assert letter_grade(85) == "B"
assert letter_grade(80) == "B"
assert letter_grade(79.5) == "C"
assert letter_grade(72) == "C"
assert letter_grade(70) == "C"
assert letter_grade(69) == "D"
assert letter_grade(60) == "D"
assert letter_grade(59) == "F"
assert letter_grade(10) == "F"
assert letter_grade(1) == "F"
assert letter_grade(0) == "F"
print("OK")
