"""
"[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has survived to the present day."
-- Donald Knuth, The Art of Computer Programming, Vol. 2: Seminumerical Algorithms, 2nd edition (1981).

The greatest common divisor (GCD), also known as the greatest common factor of two or more integers (at least one of which is not zero), is the largest positive integer that divides a number without a remainder. For example, the GCD of 8 and 12 is 4.

You are given an arbitrary number of positive integers. You should find the greatest common divisor for these numbers.

Input: An arbitrary number of positive integers.

Output: The greatest common divisor as an integer.

Example:

greatest_common_divisor(6, 4) == 2
greatest_common_divisor(2, 4, 8) == 2
greatest_common_divisor(2, 3, 5, 7, 11) == 1
greatest_common_divisor(3, 9, 3, 9) == 3

Precondition:
1 < len(args) ≤ 10
all(0 < x ≤ 2 ** 32 for x in args)
"""

def greatest_common_divisor(*args:int) -> int:
    res = args[0]
    for x in args[1:]:
        _m = max(x, res)
        _n = min(x, res)
        while True:
            _r = _m % _n
            if _r == 0:
                res = _n
                break
            _m = max(_n, _r)
            _n = min(_n, _r)
    return res


if __name__ == '__main__':
    print("Example:")
    print(greatest_common_divisor(6, 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert greatest_common_divisor(6, 4) == 2
    assert greatest_common_divisor(2, 4, 8) == 2
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1
    assert greatest_common_divisor(3, 9, 3, 9) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
