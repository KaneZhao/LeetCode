/**
 * 
 * Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
 */
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, res = 0, minLen = 0;
        for (int right = 0; right < nums.length; ++right){
            res += nums[right];
            while (res >= target){
                if ((minLen > 0 && right - left + 1 < minLen) || minLen == 0){
                    minLen = right - left + 1;
                }    
                res -= nums[left++];
            }
        }
        return minLen;
    }
}
