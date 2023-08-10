/**
 * 
 * Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
         if (root == null) {
            return true;
         } else {
            return isSymmetricHelper(root.left, root.right);
         }
    }

    public boolean isSymmetricHelper(TreeNode left, TreeNode right) {
        if (left == null || right == null) {
            if (left == null && right == null) {
                return true;
            } else {
                return false;
            }
        } else {
            if (left.val != right.val) {
                return false;
            } else {
                return isSymmetricHelper(left.left, right.right) && isSymmetricHelper(left.right, right.left);
            }
        }
    }
}