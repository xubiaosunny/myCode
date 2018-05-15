"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = len(s)
        m = l

        if numRows == 1:
            return s
        
        s_map = [['' for i in range(m)] for j in range(numRows)]
        
        x = 0
        y = 0
        
        is_up = False
        
        for ss in s:
            s_map[y][x] = ss
            
            if y == numRows - 1:
                is_up = True
            if y == 0:
                is_up = False
            
            if is_up:
                y -= 1 
                x += 1 
            else:
                y += 1 
        
        s_list = []
        for n_list in s_map:
            s_list.extend(n_list)

        return ''.join(s_list)
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("AB", 1) == 'AB')
    