"""
"Fizz buzz" 是一个单词游戏，我们将教会机器人学会关于除法的一些知识。

你将要使用python写一个方法，方法接收一个整数，然后返回：
"Fizz Buzz" 如果这个整数可以整除3并且可以整除5；
"Fizz" 如果整个整数可以整除3；
"Buzz" 如果这个整数可以整除5；
其他情况则返回传入的这个整数；
输入: 一个整数值。

输出: 一个字符串类型的答案。

举个栗子:

checkio(15) == "Fizz Buzz"
checkio(6) == "Fizz"
checkio(5) == "Buzz"
checkio(7) == "7"

你将学到什么: 这个任务可以让你学会写一个十分简单的方法，并学会使用if-else 语句。

Precondition: 0 < number ≤ 1000
"""


def checkio(number: int) -> str:
    res = []
    if number % 3 == 0:
        res.append('Fizz')
    if number % 5 == 0:
        res.append('Buzz')
    return ' '.join(res) if res else str(number)

# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio(15))
    
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
