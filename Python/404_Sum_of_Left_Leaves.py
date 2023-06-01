"""
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(root):
            nonlocal res
            if root is None:
                return    
            if root.left is not None and root.left.left is None and root.left.right is None:
                res += root.left.val
            traverse(root.left)
            traverse(root.right) 
        traverse(root)  
        return res             