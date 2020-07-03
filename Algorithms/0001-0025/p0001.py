class Solution:
    def twoSum(self, nums, target):
        numsDict = dict()
        for i in range(len(nums)):
            numsDict[nums[i]] = numsDict.get(nums[i], []) + [i]

        for i in numsDict.keys():
            temp = target - i
            if temp == i and len(numsDict[i]) > 1:
                return numsDict[i][:2]
            elif temp != i and temp in numsDict:
                return numsDict[i][:1] + numsDict[temp][:1]
