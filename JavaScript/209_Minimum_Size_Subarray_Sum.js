/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function (target, nums) {
  let left = 0,
    res = 0,
    minLen = 0;
  for (let right = 0; right < nums.length; right++) {
    res += nums[right];
    while (res >= target) {
      if ((minLen > 0 && right - left + 1 < minLen) || minLen === 0) {
        minLen = right - left + 1;
      }
      res -= nums[left++];
    }
  }
  return minLen;
};
