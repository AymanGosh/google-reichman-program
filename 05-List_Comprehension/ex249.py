def funny2(s):
    words = s.split()
    filterd_words = [w.lower() for w in words if "!" not in w]
    reverse_filterd_words = [(w[::-1]).capitalize() for w in filterd_words]
    return " ".join(reverse_filterd_words)


result = funny2("Foo bar! I said bar!")
print(result)
assert result == "Oof I Dias"

result = funny2("The qu!ck brown fox")
print(result)
assert result == "Eht Nworb Xof"

print("OK")
