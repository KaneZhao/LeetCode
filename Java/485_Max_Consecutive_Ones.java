/**
 * Given a binary array nums, return the maximum number of consecutive 1's in the array.
 * 
 */

// This question is about finding the maximum number of consecutive 1s. It is not a difficult problem. You can traverse the array and use a counter cnt to count the number of 1s. If the current number is 0, then cnt is reset to 0. If it is not 0, cnt is incremented by 1, and then the result res is updated each time. 
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int res = 0, cur = 0;
        for (int num : nums) {
            if (num == 1) {
                cur++;
            } else {
                res = (res > cur) ? res : cur;
                cur = 0;
            }
        }
        return (res > cur) ? res : cur;
    }
}