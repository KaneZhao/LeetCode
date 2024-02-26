"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""

# We can use Dynamic Programming to solve the problem. Create a one-dimensional dp array of length n+1, initialise the first value to 0 and the rest of the values to 10000. i loops from 0 to n, j loops from 1 to where i+j*j <= n, and then updates dp[i+j*j] each time. 
# Dynamic programming dp array dp[i] that positive integer i can be composed of at least multiple perfect squares, then we seek n, is to return dp[n] can be. Note that i must start from 0, j must start from 1, because our original intention is to use dp[i] to update dp[i + j * j], if i=0, j=1, then dp[i] and dp[i + j * j] will be equal!

class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [10000] * (n + 1)
        dp[0] = 0
        for i in range(0, n + 1):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
                j += 1
        return dp[n]         
        