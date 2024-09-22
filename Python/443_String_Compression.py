"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        chars.append(None)    
        left, right = 0, 1
        cnt, cur = 1, chars[left]
        while right < len(chars):
            if chars[right] == cur:
                cnt += 1
            else:
                if cnt != 1:
                    while cnt > 0:
                        left += 1
                        if cnt // 1000 != 0:
                            chars[left] = str(cnt // 1000)
                            cnt = cnt % 1000
                            if cnt == 0:
                                for i in range(3):
                                    left += 1
                                    chars[left] = "0"
                        elif cnt // 100 != 0:
                            chars[left] = str(cnt // 100)
                            cnt = cnt % 100
                            if cnt == 0:
                                for i in range(2):
                                    left += 1
                                    chars[left] = "0"
                        elif cnt // 10 != 0: 
                            chars[left] = str(cnt // 10)    
                            cnt = cnt % 10
                            if cnt == 0:
                                for i in range(1):
                                    left += 1
                                    chars[left] = "0"
                        else:
                            chars[left] = str(cnt)
                            cnt = 0   
                left += 1
                cur = chars[right]
                chars[left] = cur 
                cnt = 1 
            right += 1
        return left                  



        