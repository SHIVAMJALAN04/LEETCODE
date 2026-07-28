class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        a = len(s)
        for i in range(a // 2):
            if s[i] != s[a - 1 - i]:
                return False
        return True