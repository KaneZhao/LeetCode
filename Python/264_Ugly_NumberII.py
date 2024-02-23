"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.
"""

# 1.The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
# 2.An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
# 3.The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
# 4.Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        res, l2, l3, l5 = [1], [], [], []
        i2, i3, i5 = 0, 0, 0
        for i in range(2,n+1):
            l2.append(res[-1] * 2)
            l3.append(res[-1] * 3)
            l5.append(res[-1] * 5)
            min_val = min(l2[i2], l3[i3], l5[i5])
            if min_val == l2[i2]:
                i2 += 1
            if min_val == l3[i3]:
                i3 += 1
            if min_val == l5[i5]:
                i5 += 1
            res.append(min_val)
        return res[-1]                