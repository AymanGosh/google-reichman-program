def progress_bar(width, total, completed):
    progress = completed / total
    num_hashes = int(progress * width)
    num_dashes = width - num_hashes
    bar = "#" * num_hashes + "-" * num_dashes
    return bar


def advanced_progress_bar(width, total, completed):
    bar = progress_bar(width - 7, total, completed)
    return "|" + bar + "|" + " {:3}".format(int(completed / total * 100)) + "%"


result = advanced_progress_bar(17, 100, 32)

print(result)
assert result == "|###-------|  32%"

result = advanced_progress_bar(17, 100, 5)
print(result)
assert result == "|----------|   5%"

result = advanced_progress_bar(20, 10, 4)
print(result)
assert result == "|#####--------|  40%"

result = advanced_progress_bar(30, 1000, 260)
print(result)
assert result == "|#####------------------|  26%"

result = advanced_progress_bar(13, 85, 85)
print(result)
assert result == "|######| 100%"

result = advanced_progress_bar(13, 85, 0)
print(result)
assert result == "|------|   0%"

result = advanced_progress_bar(13, 1000, 999)
print(result)
assert result == "|#####-|  99%"

print()
print()

print(advanced_progress_bar(20, 5, 0))
print(advanced_progress_bar(20, 5, 1))
print(advanced_progress_bar(20, 5, 2))
print(advanced_progress_bar(20, 5, 3))
print(advanced_progress_bar(20, 5, 4))
print(advanced_progress_bar(20, 5, 5))

print()
print("OK!")
