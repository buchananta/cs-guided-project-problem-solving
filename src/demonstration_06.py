"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = 0
    for c in input_str:
        # and this is why I love weakly typed languages
        res += c in vowels
    return res

def get_countInstructor(input_str: str) -> int:
    num_vowels = 0
    vowels = "aeiou"
    for char in input_str:
        if char in vowels:
            num_vowels += 1
    return num_vowels
