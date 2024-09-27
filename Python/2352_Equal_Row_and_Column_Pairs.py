"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dic, col_dic = {}, {}
        cnt = 0
        for i in grid:
            key = '_'.join(str(num) for num in i)
            row_dic[key] = row_dic.get(key, 0) + 1
        for j in range(len(grid[0])):
            key = '_'.join([str(row[j]) for row in grid])
            col_dic[key] = col_dic.get(key, 0) + 1
        for k in row_dic.keys():
            if k in col_dic:
                cnt += row_dic[k] * col_dic[k]
        return cnt        
        