# company_flat1.py
from pprint import pprint
import json



def total_salaries(people):
    # ---- YOUR CODE HERE -----------------
    sum(p["salary"] for p in people)

    # sum = 0
    # for p in people:
    #     sum += p["salary"]
    return sum(p["salary"] for p in people)
    pass
    # -------------------------------------


def total_salaries_for_position(people, position):
    # ---- YOUR CODE HERE -----------------
    # sum = 0
    # for p in people:
    #     if p["position"] == position:
    #         sum += p["salary"]


    return  sum(p["salary"] for p in people if p["position"] == position)
    pass
    # -------------------------------------


with open("company1.json") as f:
    all_employees = json.load(f)
pprint(all_employees)


result1 = total_salaries(all_employees)
print("Total salary:", result1)
assert result1 == 1979800
print("OK1")

result2 = total_salaries_for_position(all_employees, "Developer")
print("Developers' salary:", result2)
assert result2 == 1073700
print("OK2")

result3 = total_salaries_for_position(all_employees, "Team Leader")
print("Team Leaders' salary:", result3)
assert result3 == 376100
print("OK3")

print("Done!")