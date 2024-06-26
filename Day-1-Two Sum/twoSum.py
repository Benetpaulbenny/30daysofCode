class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapDict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapDict:
                return [mapDict[complement], i]
            mapDict[nums[i]] = i