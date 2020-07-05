# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()
        for i in range(len(nums)):
            numsDict[nums[i]] = numsDict.get(nums[i], []) + [i]

        for i in numsDict.keys():
            temp = target - i
            if temp == i and len(numsDict[i]) > 1:
                return numsDict[i][:2]
            elif temp != i and temp in numsDict:
                return numsDict[i][:1] + numsDict[temp][:1]


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 3], 6))
print(Solution().twoSum([2, 5, 5, 11], 10))
print(Solution().twoSum([2, 5, 11, 5], 10))
print(Solution().twoSum([3, 2, 4], 6))
