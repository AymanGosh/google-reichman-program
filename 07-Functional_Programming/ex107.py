import time


CACHE = None

def calculate_life():
    global CACHE
    if( CACHE is None):
        time.sleep(3)
        CACHE = 42
    return CACHE


print("start")

for n in range(5):
    print(calculate_life())
for n in range(5):
    print(calculate_life())

print("done")