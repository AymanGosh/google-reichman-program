import time


def trace(f):
    def df(*args, **kwargs):
        print(f">>> ENTER '{f.__name__}'; args={args}; kwargs={kwargs}")

        result = f(*args, **kwargs)

        print(f"<<< EXIT '{f.__name__}'; result {type(result).__name__}: {result!r}")

        return result

    return df


@trace
def foo():
    print("=== IN FOO")
    return 123


@trace
def bar(x, y):
    print("=== IN BAR")
    time.sleep(0.5)
    return x + y


print("---[Part 1]---")
result1 = foo()
print(f"--- Result #1: {result1!r}")
print()

print("---[Part 2]---")
result2 = bar(10, 20)
print(f"--- Result #2: {result2!r}")
print()

print("---[Part 3]---")
result3 = bar(y=10, x=20)
print(f"--- Result #3: {result3!r}")






def my_profile(f):

    def in_f(*args, **kwargs):
        return f(*args, **kwargs)

    return in_f

@my_profile
def foo():
    print("=== IN FOO")
    return 123


@my_profile
def bar(x, y):
    print("=== IN BAR")
    time.sleep(0.5)
    return x + y


print("---[Part 1]---")
result1 = foo()
print(f"--- Result #1: {result1!r}")

print()

print("---[Part 2]---")
result2 = bar(10, 20)
print(f"--- Result #2: {result2!r}")

print()

print("---[Part 3]---")
result3 = bar(y=10, x=20)
print(f"--- Result #3: {result3!r}")

print()
print("Done.")