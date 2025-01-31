# funny_reverse.py


def funny(s):
    separated_words = s.split()
    result = []
    for w in separated_words:
        result.append(w[::-1].capitalize())
    final_sent = " ".join(result)
    return final_sent


def funny(s):
    return " ".join([w[::-1].capitalize() for w in s.split()])


result_1 = funny("Foo bar")
print("Result 1:", result_1)

assert result_1 == "Oof Rab"

result_2 = funny("The quick brown fox")
print("Result 2:", result_2)
assert result_2 == "Eht Kciuq Nworb Xof"

print("OK")
