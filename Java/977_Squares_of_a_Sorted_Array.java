/**
 * Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 * 
 */

 class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] res = new int[nums.length];
        int left = 0, right = nums.length - 1, len = nums.length - 1;
        while (left <= right) {
            if (Math.abs(nums[left]) > Math.abs(nums[right])){
                res[len] = nums[left] * nums[left];
                left++;
            } else {
                res[len] = nums[right] * nums[right];
                right--;
            }
            --len;
        }
        return res;
    }
}