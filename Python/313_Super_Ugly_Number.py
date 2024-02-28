"""
A super ugly number is a positive integer whose prime factors are in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp, lst = [2**32 - 1] * n, [0] * len(primes)
        dp[0] = 1
        for i in range(1, n):
            for j in range(0, len(lst)):
                dp[i] = min(dp[i], dp[lst[j]] * primes[j])
            for j in range(0, len(lst)):
                if dp[i] == dp[lst[j]] * primes[j]:
                    lst[j] += 1
        return dp[-1]                

        