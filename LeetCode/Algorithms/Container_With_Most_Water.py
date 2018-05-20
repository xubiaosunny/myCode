"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0

        start = 0
        end = len(height) - 1

        while True:
            w = end - start
            h = min(height[start], height[end])
            water = w * h

            if water > max_water:
                max_water = water

            if w == 1:
                break
            else:
                if height[start] > height[end]:
                    end -= 1
                else:
                    start += 1

        return max_water


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1, 1]) == 1)
