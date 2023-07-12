"""
Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3 * ... * x and by convention, 0! = 1.

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has two zeroes at the end.
Given an integer k, return the number of non-negative integers x have the property that f(x) = k.
"""
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        return int(self.right_bound(k) - self.left_bound(k) + 1)

    def left_bound(self, target: int) -> int:
        lo, hi = 0, 10e9
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.trailingZeroes(mid) < target:
                lo = mid + 1
            elif self.trailingZeroes(mid) > target:
                hi = mid
            else:
                hi = mid
        return lo
    
    def right_bound(self, target: int) -> int:
        lo, hi = 0, 10e9
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.trailingZeroes(mid) < target:
                lo = mid + 1
            elif self.trailingZeroes(mid) > target:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1    

    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res        