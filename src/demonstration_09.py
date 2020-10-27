"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
import math
def get_middle(input_str):
    # Your code here
    start = math.floor((len(input_str) -1) / 2)
    end = math.ceil((len(input_str) -1) / 2)
    return input_str[start:end + 1]


def is_even(n: int) -> bool:
    return n % 2 == 0
def get_middleInstructor(input_str: str) -> str:
    if is_even(len(input_str)):
        midpoint = len(input_str) // 2
        return input_str[midpoint -1 : midpoint + 1]
    else:
        midpoint = len(input_str) // 2
        return input_str[midpoint]
