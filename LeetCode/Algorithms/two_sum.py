# -*- coding: utf-8 -*-
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            res = target - n
            if res in nums:
                j = nums.index(res)
                if i != j:
                    return [i, j]
        else:
            return []


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9) == [0, 1])
