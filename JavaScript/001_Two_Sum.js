/**
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let numberMap = new Map();

    for (let index = 0; index < nums.length; index++) {
        val = nums[index];

    if (numberMap.has(target - val)) 
        return [index, numberMap.get(target - val)];
    else numberMap.set(val, index);
    }

    return [];
};