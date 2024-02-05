class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length <= 0){
            return 0;
        }
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            if (nums[left] == val) {
                if (nums[right] == val) {
                    right--;
                } else{
                    int tmp = nums[left];
                    nums[left] = nums[right];
                    nums[right] = tmp;
                }
            } else {
                left++;
            }
        }
        return left;       
    }
}