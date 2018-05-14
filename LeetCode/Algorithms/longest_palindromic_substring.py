class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        max_ss = ""
        
        for x in range(l):
            tmp_ss = self.expand_around_center(s, x, x)
            if len(tmp_ss) > len(max_ss):
                max_ss = tmp_ss
                
            if x < l - 1:    
                tmp_ss = self.expand_around_center(s, x, x + 1)
                if len(tmp_ss) > len(max_ss):
                    max_ss = tmp_ss
                    
        return max_ss
    
    def expand_around_center(self, s, x, y):
        while x >= 0 and y < len(s) and s[x] == s[y]:
            x -= 1
            y += 1
        return s[x + 1:y] 

if __name__  == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("a") == 'a')
