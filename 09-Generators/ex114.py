# simple_generator2.py

def intputs(prompt=">> ", invalid_message="Invalid input"):
     yield 0
     print("")


for x in intputs():
    print(x if x % 7 else "Boom!")
print("Done!")