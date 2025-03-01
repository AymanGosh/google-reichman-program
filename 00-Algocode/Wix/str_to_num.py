from typing import Dict

# Mapping of word numbers to digits
word_to_num: Dict[str, str] = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def convert_to_numeric(s: str) -> str:
    result = []
    word = ""

    for char in s:
        if char.isdigit():  # If it's a digit, append directly
            if word:  # Convert any accumulated word
                result.append(word_to_num.get(word, ""))
                word = ""
            result.append(char)
        else:  # It's a letter, accumulate
            word += char
            if word in word_to_num:  # If it's a valid number word
                result.append(word_to_num[word])
                word = ""  # Reset word buffer

    return "".join(result)

def compare_strings(str1: str, str2: str) -> int:
    num1 = int(convert_to_numeric(str1))
    num2 = int(convert_to_numeric(str2))

    return -1 if num1 > num2 else 1 if num1 < num2 else 0

# Example usage:
print(compare_strings("one2three", "two1three"))  # Output: 1 (112 < 213)
print(compare_strings("three4", "34"))  # Output: 0 (34 == 34)
print(compare_strings("nine", "eight"))  # Output: -1 (9 > 8)
