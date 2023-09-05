"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def traverse(root, lst):
            if not root.left and not root.right:
                res.append('->'.join(lst))
                return

            if root.left:
                lst.append(str(root.left.val))
                traverse(root.left, lst)
                lst.pop()

            if root.right:
                lst.append(str(root.right.val))
                traverse(root.right, lst)
                lst.pop()
            return

        if not root:
            return []
        res = []
        traverse(root, [str(root.val)])
        return res            

            