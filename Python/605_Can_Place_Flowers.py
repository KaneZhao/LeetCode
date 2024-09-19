"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

"""
If there are 3 consecutive zeros, 000, how many pots of flowers can be placed? In fact, it depends on the positions on the left and right. If it is 10001, then only 1 pot can be placed. If the flowers on the left and right are borders, then two pots can be placed, 101. Therefore, if we want to calculate the number of flowers that can be placed by counting the number of consecutive 0s, we must process the borders. The processing method is to add a 0 in front if the first position is 0, and add a 0 at the end if the last position is 0. After this processing, we assume that the left and right sides of the consecutive 0s are 1. In this way, if there are k consecutive 0s, then the number of flowers that can be placed can be quickly calculated by (k-1)/2
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0,0)
        flowerbed.append(0)
        res, cnt = 0, 0
        for i in flowerbed:
            if i == 0:
                cnt += 1
            else:
                res += (cnt - 1) // 2
                cnt = 0
        res += (cnt - 1) // 2        
        return res >= n            

            
        