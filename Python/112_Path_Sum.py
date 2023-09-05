"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(root, count):
            if not root.left and not root.right and count == 0:
                return True
            if not root.left and not root.right:
                return False

            if root.left:
                count -= root.left.val
                if traverse(root.left, count):
                    return True
                count += root.left.val

            if root.right:
                count -= root.right.val
                if traverse(root.right, count):
                    return True
                count += root.right.val   

            return False

        if not root:
            return False
        return traverse(root, targetSum - root.val)                
