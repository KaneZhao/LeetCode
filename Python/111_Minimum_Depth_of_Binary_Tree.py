"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res, depth = 100000, 0
        if not root:
            return 0
        def traverse(root):
            nonlocal res, depth
            if root is None:
                return
            depth += 1
            if root.left is None and root.right is None:
                res = min(res, depth)
            traverse(root.left)
            traverse(root.right)
            depth -= 1
        traverse(root)
        return res   
        