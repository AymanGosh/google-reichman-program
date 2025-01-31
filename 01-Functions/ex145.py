def simple_progress_bar(completed):
    progress_bar = "----------"
    if completed > 10:
        return progress_bar
    return "#" * completed + progress_bar[completed::]


result = simple_progress_bar(3)
print(result)
assert result == "###-------"

result = simple_progress_bar(10)
print(result)
assert result == "##########"

result = simple_progress_bar(0)
print(result)
assert result == "----------"

print()
print()

print(simple_progress_bar(0))
print(simple_progress_bar(1))
print(simple_progress_bar(2))
print(simple_progress_bar(3))
print(simple_progress_bar(4))
print(simple_progress_bar(5))
print(simple_progress_bar(6))
print(simple_progress_bar(7))
print(simple_progress_bar(8))
print(simple_progress_bar(9))
print(simple_progress_bar(10))

print()
print("OK!")
