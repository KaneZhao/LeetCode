class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 1) {
            return 1;
        }
        int i = 1, target = nums[0];
        for (int j = 1; j < nums.length; ++j) {
            if (nums[j] != target) {
                nums[i] = nums[j];
                target = nums[j];
                i++;
            }
        }
        return i;
    }
}