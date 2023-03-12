class Solution:
    def reverse(self, x: int) -> int:
        tmp, res = abs(x), 0
        while tmp > 0:
            res = res * 10 + tmp % 10
            if res > 2147483647 or res < -2147483648:
                return 0
            tmp = tmp // 10
        return res if x > 0 else -res
