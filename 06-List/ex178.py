def country_letter_grade(system, score):
    grade_mappings = system.split(",")
    print(grade_mappings)
    for mapping in grade_mappings:
        grade, lowest_score = mapping.split(":")
        print(mapping.split(":"), grade, lowest_score)
        if score >= float(lowest_score):
            return grade

    return "Invalid"


# Grading systems
JAPAN = "AA:90,A:80,B:70,C:60,F:0"
THAILAND = "A:80,B+:75,B:70,C+:65,C:60,D+:55,D:50,F:0"
ICELAND = "A:94,B+:82,B:65,C+:50,C:35,D:1,O:0"
IRELAND = "A:85,B:70,C:55,D:40,E:25,F:1,NG:0"
US_4 = "A:92,B:83,C:74,D:65,F:0"
US_12 = "A+:97,A:93,A-:90,B+:87,B:83,B-:80,C+:77,C:73,C-:70,D+:67,D:63,D-:60,F:0"

# Test cases
# assert country_letter_grade(JAPAN, 100) == "AA"
# assert country_letter_grade(THAILAND, 100) == "A"
# assert country_letter_grade(US_12, 100) == "A+"
# assert country_letter_grade(JAPAN, 90) == "AA"
# assert country_letter_grade(THAILAND, 90) == "A"
# assert country_letter_grade(US_12, 90) == "A-"
# assert country_letter_grade(US_4, 90) == "B"
# assert country_letter_grade(ICELAND, 85) == "B+"
# assert country_letter_grade(ICELAND, 80) == "B"
# assert country_letter_grade(THAILAND, 79.5) == "B+"
# assert country_letter_grade(IRELAND, 72) == "B"
# assert country_letter_grade(US_12, 72) == "C-"
# assert country_letter_grade(ICELAND, 60) == "C+"
assert country_letter_grade(JAPAN, 10) == "F"
# assert country_letter_grade(JAPAN, 0) == "F"
# assert country_letter_grade(ICELAND, 0) == "O"
# assert country_letter_grade(IRELAND, 10) == "F"
# assert country_letter_grade(IRELAND, 0) == "NG"

print("OK")
