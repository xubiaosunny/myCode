"""
你本关的任务是检查给定的列表，判断是否其中所有的元素都相等。

输入: 列表

输出: 布尔值

范例:

    all_the_same([1, 1, 1]) == True
    all_the_same([1, 2, 1]) == False
    all_the_same(['a', 'a', 'a']) == True
    all_the_same([]) == True

本关创意来自 Python Tricks series by Dan Bader

前提: 输入的列表中的所有元素均是可哈希的。
"""


from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")