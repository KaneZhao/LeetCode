"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traverse(root, count, lst):
            if not root.left and not root.right and count == 0:
                res.append(lst[:])
                return 
            if not root.left and not root.right:
                return
            if root.left:
                count -= root.left.val
                lst.append(root.left.val)
                traverse(root.left, count, lst) 
                lst.pop()
                count += root.left.val 
            if root.right:
                count -= root.right.val
                lst.append(root.right.val)
                traverse(root.right, count, lst) 
                lst.pop()
                count += root.right.val   
            return 
            
        if not root:
            return []        
        res = []
        traverse(root, targetSum - root.val, [root.val])   
        return res              
        