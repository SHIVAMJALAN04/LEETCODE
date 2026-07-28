class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        s = str(abs(x))
        rev = int(s[::-1])
        rev *= sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev