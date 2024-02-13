"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        i, j = 0, 0
        num = 1
        while True:
            while j < n - 1 and res[i][j + 1] == 0:
                res[i][j] = num
                j += 1
                num += 1
            while i < n - 1 and res[i + 1][j] == 0:
                res[i][j] = num
                i += 1    
                num += 1
            while j > 0 and res[i][j - 1] == 0:
                res[i][j] = num
                j -= 1
                num += 1
            while i > 0 and res[i - 1][j] == 0:
                res[i][j] = num
                i -= 1
                num += 1
            if num >= n * n:
                break
        res[i][j] = num    
        return res                    


        