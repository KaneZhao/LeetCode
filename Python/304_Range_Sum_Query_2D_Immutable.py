"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
"""
class NumMatrix:
    base = None
    def __init__(self, matrix: List[List[int]]):
        self.base = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j > 0:
                    self.base[i][j] = self.base[i][j - 1] + matrix[i][j]
                elif j == 0 and i > 0:
                    self.base[i][j] = self.base[i - 1][j] + matrix[i][j]
                elif i > 0 and j > 0:
                    self.base[i][j] = self.base[i - 1][j] + self.base[i][j - 1] - self.base[i - 1][j - 1] + matrix[i][j]   
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.base[row2][col2]
        elif row1 == 0:
            return self.base[row2][col2] - self.base[row2][col1 - 1]
        elif col1 == 0:
            return self.base[row2][col2] - self.base[row1 - 1][col2]
        else:
            return self.base[row2][col2] - self.base[row1 - 1][col2] - self.base[row2][col1 - 1] + self.base[row1 - 1][col1 - 1]           
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)