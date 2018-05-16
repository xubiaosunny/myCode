"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def int32_check(i):
            if -2 ** 31 <= i <= 2 ** 31 - 1:
                return i
            return 0

        if x > 0:
            return int32_check(int(str(x)[::-1]))
        elif x < 0:
            return int32_check(-int(str(abs(x))[::-1]))
        else:
            return x


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123) == 321)
    print(solution.reverse(1534236469) == 0)
