##python -m black C:/Users/aymn-/PycharmProjects/PythonProject/formatiinglesson.py


def f1(s: str) -> int:
    x = 10
    return 1


# funny_reverse.py

def funny(s):
    s = s.split(" ")
    for w in s :
        w = w[::-1]
        print(w)

    print(s)
    return s


result_1 = funny("Foo bar")
print("Result 1:", result_1)

assert result_1 == "Oof Rab"

result_2 = funny("The quick brown fox")
print("Result 2:", result_2)
assert result_2 == "Eht Kciuq Nworb Xof"

print("OK")
