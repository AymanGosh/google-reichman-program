def nachmanize(word):
    nachmanize_word = ""
    for i in range(len(word)):
        nachmanize_word += word[: i + 1] + " "
    return nachmanize_word.strip()


result = nachmanize("abcd")
print(result)
assert result == "a ab abc abcd"

result = nachmanize("shalom")
print(result)
assert result == "s sh sha shal shalo shalom"

print("OK")
