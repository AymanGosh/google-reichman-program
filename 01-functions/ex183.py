def automaton_126(s):
    n = len(s)
    result = []
    for i in range(n):
        left = s[(i - 1) % n]
        middle = s[i]
        right = s[(i + 1) % n]
        if (left == middle == right == "X") or (left == middle == right == "."):
            result.append(".")
        else:
            result.append("X")
    return "".join(result)


assert automaton_126("...") == "..."
assert automaton_126("XXX") == "..."
assert automaton_126("...X..X...") == "..XXXXXX.."
assert automaton_126(".....X.....") == "....XXX...."
assert automaton_126("X..........") == "XX........X"
assert automaton_126("..........X") == "X........XX"
assert automaton_126(".XX.X.X..X.X.X") == "XXXXXXXXXXXXXX"
assert automaton_126("...X..X..") == "..XXXXXX."
print("Tests OK")
