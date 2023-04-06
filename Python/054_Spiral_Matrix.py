"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        while True:
            while j < n - 1 and matrix[i][j + 1] != 200:
                res.append(matrix[i][j])
                matrix[i][j] = 200
                j += 1
            while i < m - 1 and matrix[i + 1][j] != 200:
                res.append(matrix[i][j])
                matrix[i][j] = 200
                i += 1
            while j > 0 and matrix[i][j - 1] != 200:
                res.append(matrix[i][j])
                matrix[i][j] = 200
                j -= 1
            while i > 0 and matrix[i - 1][j] != 200:
                res.append(matrix[i][j])
                matrix[i][j] = 200
                i -= 1     
            if len(res) == m * n - 1:
                break
        res.append(matrix[i][j])
        return res               