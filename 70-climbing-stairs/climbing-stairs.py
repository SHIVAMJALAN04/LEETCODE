import math
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n>45:
            return 0
        else:
            count=0
            y=n//2
            for k in range(0,y+1):
                i=n
                i=(i-2*k)
                j=k
                z=i+j
                count+= math.factorial(z) // (math.factorial(j) * math.factorial(z-j))
            return count
