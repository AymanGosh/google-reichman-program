import time


class MyProfiler:
    def __init__(self, name: str):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


print("--- Part 1 ---")
print("> Before Block")
with MyProfiler("foo") as c:
    time.sleep(0.5)
    print("> In Block")
print("> After Block")

print()

print("--- Part 2 ---")
with MyProfiler("bar") as c:
    time.sleep(0.5)
    print(f"Elapsed: {c.elapsed():.1f}s.")
    time.sleep(0.5)

print()

print("--- Part 3 ---")
with MyProfiler("baz") as c:
    time.sleep(0.5)
    1 / 0

x = time.perf_counter()
time.sleep(1)
y = time.perf_counter()


print(y-x)

