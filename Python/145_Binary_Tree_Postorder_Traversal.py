"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(root):
            if root is None:
                return 
            traverse(root.left)
            traverse(root.right)
            res.append(root.val)
        traverse(root)
        return res      