class Solution {
    public int[] productExceptSelf(int[] nums) {
        int nLen = nums.length;
        int[] left = new int[nLen];
        int[] right = new int[nLen];
        for (int i = 0; i < nLen; ++i){
            if (i == 0){
                left[i] = nums[i];
                right[nLen - i - 1] = nums[nLen - i - 1];
            }else {
                left[i] = left[i - 1] * nums[i];
                right[nLen - i - 1] = right[nLen - i] * nums[nLen - i - 1];
            }            
        }
        for (int i = 0; i < nLen; ++i){
            if (i == 0){
                nums[i] = right[i + 1];
            } else if(i == nLen - 1){
                nums[i] = left[i - 1];
            } else{
                nums[i] = left[i - 1] * right[i + 1];
            }
        }
        return nums;               
    }
}