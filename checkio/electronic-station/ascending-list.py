"""
Determine whether the sequence of elements items is ascending so that its each element is strictly larger than (and not merely equal to) the element that precedes it.

Input: Iterable with ints.

Output: Bool.

Example:

is_ascending([-5, 10, 99, 123456]) == True
is_ascending([99]) == True
is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
is_ascending([]) == True
is_ascending([1, 1, 1, 1]) == False
1
2
3
4
5
The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
"""

from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    for i, x in enumerate(items[:-1]):
        if x >= items[i + 1]:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")