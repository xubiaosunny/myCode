# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        i = 0
        max_len = 0
     
        while True:
            for x in range(i + max_len + 1, l + 1):
                current_len = len(s[i:x])
                if len(set(s[i:x])) == current_len:
                    if current_len > max_len:
                        max_len = current_len
                else:
                    i += 1
                    break
            if l - i <= max_len:
                break
                
        return max_len


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew") == 3)
