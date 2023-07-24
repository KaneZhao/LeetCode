"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
"""

"""
The core idea is to use a HashMap to establish a mapping between characters and their frequencies of occurrence.
Since we are dealing with only lowercase letters, we can use an array of size 26 instead of a HashMap.
We traverse from 0 to 25 for each position, updating the 'base' array with the minimum value between the current value and the corresponding value in array 'word_cnt'.
"""
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res, base = [], [101] * 26
        for word in words:
            word_cnt = [0] * 26
            for char in word:
                word_cnt[ord(char) - ord('a')] += 1
            for i in range(len(base)):
                base[i] = min(base[i], word_cnt[i])
        for i in range(len(base)):
            for _ in range(base[i]):
                res.append(chr(i + ord('a')))
        return res                    
