def smart_sum(data):

    if type(data) == int:
        return data
    if len(data) == 0:
        return 0

    return smart_sum(data[0]) + smart_sum(data[1:])


def smart_sum2(data):
    # with list comprehension
    # ----- YOUR CODE HERE -----
    pass
    # --------------------------


example = [
    100,
    [
        10,
        [
            20,
            30,
        ],
        40,
    ],
    100,
    [
        10,
        [50, [20, 20, 20]],
    ],
    12,
]

total = smart_sum([100, 200, 300])
assert total == 600
print(total)
print("OK0")

total = smart_sum(example)
assert total == 432
print(total)
print("OK1")


print("Done!")
