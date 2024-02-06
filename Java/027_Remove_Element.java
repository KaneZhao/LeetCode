/**
 * Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

  Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

  Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
  Return k.
 * 
 */

class Solution {
    public int removeElement(int[] nums, int val) {
        if (nums.length <= 0){
            return 0;
        }
        int i = 0;
        for (int c: nums) {
            if (c != val) {
                nums[i] = c;
                i++;
            } 
        }
        return i;      
    }
}

// class Solution {
//     public int removeElement(int[] nums, int val) {
//         if (nums.length <= 0){
//             return 0;
//         }
//         int left = 0, right = nums.length - 1;
//         while (left <= right) {
//             if (nums[left] == val) {
//                 if (nums[right] == val) {
//                     right--;
//                 } else{
//                     int tmp = nums[left];
//                     nums[left] = nums[right];
//                     nums[right] = tmp;
//                 }
//             } else {
//                 left++;
//             }
//         }
//         return left;       
//     }
// }