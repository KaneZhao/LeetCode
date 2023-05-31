"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:   
        def isSymmetricHelper(left, right):
            if left is None or right is None:
                if left is None and right is None:
                    return True
                else:
                    return False
            else:
                if left.val != right.val:
                    return False
                else:    
                    return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)    
        if root is None:
            return True
        else:
            return isSymmetricHelper(root.left, root.right)                         
