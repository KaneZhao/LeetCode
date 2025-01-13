/**
 * Since the target is defined within the [left, right] interval, there are two points to note:

Use while (left <= right) because left == right is meaningful, so <= should be used.
If nums[middle] > target, right should be assigned the value middle - 1 because the current nums[middle] is definitely not the target. Therefore, the ending index of the left interval to be searched next is middle - 1.
 * 
 */
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right-left) / 2;
            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            }else {
                return mid;
            }
        }
        return -1;
    }
}