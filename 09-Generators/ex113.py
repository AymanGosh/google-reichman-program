# simple_generator1.py

def accumulate(data):
    total = 0
    for value in data:
        total += value
        yield value, total

for n, total in accumulate([100, 10, 5, 200]):
    print(n, total)

print()

for i, total in accumulate(range(1, 11)):
    print(i, total)