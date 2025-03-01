from collections import Counter

def check_words(filename, tests):
    c = Counter()
    with open(filename) as f:
        for line in f:
            word = line.strip()
            if not word:
                print("not")
            # TODO 1
            print(word)
    return c

word_tests = {
    "Words with more than 3 letters": lambda w: len(w) > 3,
    "Words with more than 5 letters": lambda w: len(w) > 5,
    "Words with the letter x": lambda w: 'x' in w,
    # TODO 2
}

results = check_words('wordsEn.txt', word_tests)

# expected = {
#     "Words with more than 3 letters": 108588,
#     "Words with more than 5 letters": 98539,
#     "Words with the letter x": 2699,
#     ........
# }

for k, v in results.items():
    print(k, v)
