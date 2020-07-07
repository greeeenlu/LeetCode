# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0
        newNums = nums1 + nums2
        length = len(newNums)
        sortedNums = sorted(newNums)
        if length % 2 == 0:
            median = (sortedNums[length // 2 - 1] + sortedNums[length // 2]) / 2
        else:
            median = sortedNums[(length - 1) // 2]
        return median
