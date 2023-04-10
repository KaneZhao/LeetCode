/**
  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
  You may assume that each input would have exactly one solution, and you may not use the same element twice.
  You can return the answer in any order.
 */

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> maps = new HashMap<>();
        for (int i = 0; i < nums.length; ++i){
            if (maps.containsKey(target - nums[i])){
                return new int[] {maps.get(target - nums[i]), i};
            } else{
                maps.put(nums[i], i);
            }
        }
        return new int[] {-1, -1};   
    }
}