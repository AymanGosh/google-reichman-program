def rotate(s):
    len_s = len(s)
    last_char = s[len_s - 1]
    new_word = last_char + s[0 : len_s - 1]
    return new_word


result = rotate("abcd")
print(result)
assert result == "dabc"

result = rotate("ello worldh")
print(result)
assert result == "hello world"

result = rotate("x")
print(result)
assert result == "x"

result = rotate(rotate(rotate("xyz")))
print(result)
assert result == "xyz"


print("OK.")
