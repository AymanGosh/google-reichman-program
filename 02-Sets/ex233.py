def solve(answer1, rows1, answer2, rows2):

    options_from_row1 = set(rows1[answer1 - 1])
    options_from_row2 = set(rows2[answer2 - 1])

    result = list(options_from_row1 & options_from_row2)

    if len(result) == 1:
        return str(result[0])

    elif len(result) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"


result = solve(
    2,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
    3,
    [
        ["1", "2", "5", "4"],
        ["3", "11", "6", "15"],
        ["9", "10", "7", "12"],
        ["13", "14", "8", "16"],
    ],
)

assert result == "7", result

result = solve(
    2,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
    2,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
)

assert result == "Bad magician!", result

result = solve(
    2,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
    3,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
)

assert result == "Volunteer cheated!", result

result = solve(
    1,
    [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "16"],
    ],
    2,
    [
        ["1", "2", "5", "4"],
        ["3", "11", "6", "15"],
        ["9", "10", "7", "12"],
        ["13", "14", "8", "16"],
    ],
)

assert result == "3", result


print("OK")
