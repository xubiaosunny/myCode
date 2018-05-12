"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
import copy


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.get_number_from_node(l1)
        n2 = self.get_number_from_node(l2)
        
        return self.create_node_from_number(n1 + n2)
        
    def get_number_from_node(self, l):
        """
        :type l: ListNode
        :rtype: int
        """
        n = ''
        while(True):
            n += str(l.val)
            if l.next is None:
                break
            l = l.next
        return int(n[::-1])
    
    def create_node_from_number(self, n):
        for i, x in enumerate(str(n)):
            if i == 0:
                l = ListNode(int(x))
            else:
                tmp = ListNode(int(x))
                tmp.next = copy.deepcopy(l) 
                l = tmp
        return l


if __name__ == "__main__":
    solution = Solution()
    