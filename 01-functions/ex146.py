def progress_bar(width, total, completed):
    progress = completed / total
    num_hashes = int(progress * width)
    num_dashes = width - num_hashes
    bar = "#" * num_hashes + "-" * num_dashes
    return bar


result = progress_bar(10, 100, 32)
print(result)
assert result == "###-------"

result = progress_bar(20, 10, 4)
print(result)
assert result == "########------------"

result = progress_bar(8, 1000, 260)
print(result)
assert result == "##------"

result = progress_bar(12, 85, 85)
print(result)
assert result == "############"

print()
print()

print(progress_bar(20, 5, 0))
print(progress_bar(20, 5, 1))
print(progress_bar(20, 5, 2))
print(progress_bar(20, 5, 3))
print(progress_bar(20, 5, 4))
print(progress_bar(20, 5, 5))

print("OK!")
