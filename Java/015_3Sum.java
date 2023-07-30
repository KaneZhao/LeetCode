/**
 * 
 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 * Notice that the solution set must not contain duplicate triplets.
 */
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
       List<List<Integer>> res = new ArrayList<>();
       Arrays.sort(nums);
       for (int i = 0; i < nums.length; ++i){
           int left = i + 1, right = nums.length - 1;
           if (i > 0 && nums[i] == nums[i - 1]){
               continue;
           }
           while (left < right){
               if (nums[i] + nums[left] + nums[right] == 0){
                   res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                   while (right > left && nums[right] == nums[right - 1]){
                       right--;
                   }
                   while (right > left && nums[left] == nums[left + 1]){
                       left++;
                   }
                   right--;
                   left++;
               }else if (nums[i] + nums[left] + nums[right] > 0){
                   right--;
               }else {
                   left++;
               }
           }
       }
       return res;         
    }
}