/**
 * You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
  Increment the large integer by one and return the resulting array of digits.
 * 
 */
class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 1, i = digits.length - 1;
        while (i >= 0) {
            if (digits[i] + carry < 10) {
                digits[i] += carry;
                return digits;
            } else {
                digits[i] = 0;
            }
            i--;
        }
        // deal with numbers like 9999
        int[] res = new int[digits.length + 1];
        res[0] = 1;
        return res;
    }
}