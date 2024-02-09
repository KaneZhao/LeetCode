// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length <= 1) {
            return;
        }
        int i = 0;
        for (int j = 0; j < nums.length; ++j) {
            if (nums[j] != 0) {
                nums[i] = nums[j];
                if (i < j) {
                    nums[j] = 0;
                }
                i++;
            }
        }
    }
}