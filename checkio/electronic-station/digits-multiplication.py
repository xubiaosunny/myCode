"""
给你一个正整数，请你写一个函数来实现：传入正整数的每一位（不包括00）的乘积

例如：给你 123405， 你应该这样处理 1*2*3*4*5=120（别忘了把0丢掉）

输入: 一个正整数.

输出: 正整数的每一位的乘积

举个栗子:

checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1
1
2
3
4
你将学到: 在这个任务中你将学会一些简单的数据类型的转换。

前提条件: 0 < number < 106
"""
from functools import reduce


def checkio(number: int) -> int:
    return reduce(lambda x, y: x * y, [int(x) for x in str(number) if x != '0'])


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")