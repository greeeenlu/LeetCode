# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeenPosition = {}
        start = 0
        length = 0

        for index, char in enumerate(s):
            print(index, char)
            if char in lastSeenPosition and lastSeenPosition[char] >= start:
                start = lastSeenPosition[char] + 1
            else:
                length = max(length, index + 1 - start)
            lastSeenPosition[char] = index
        return length


