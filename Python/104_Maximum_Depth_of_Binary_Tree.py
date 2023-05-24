"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = self.maxDepth(root.left) 
        r = self.maxDepth(root.right)
        return max(l, r) + 1    
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res, depth = 0, 0
        def traverse(root):
            nonlocal res, depth
            if root is None:
                return
            depth += 1
            if root.left is None and root.right is None:
                res = max(res, depth)
            traverse(root.left)
            traverse(root.right)
            depth -= 1
        traverse(root)
        return res     
"""    