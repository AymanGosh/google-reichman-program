import random
import time

# Generate random numbers
mylist = random.sample(range(1, 1000001), 10000)
myset = set(mylist)

# Perform lookup 10,000 times in the list
x_values = [random.randint(1, 1000000) for _ in range(10000)]
print("Starting list lookup...")
t0 = time.perf_counter()
for x in x_values:
    x in mylist
t1 = time.perf_counter()
print(f"Time for list lookup: {t1 - t0:.4f} seconds")

# Perform lookup 10,000 times in the set
print("Starting set lookup...")
t2 = time.perf_counter()
for x in x_values:
    x in myset
t3 = time.perf_counter()
print(f"Time for set lookup: {t3 - t2:.4f} seconds")
