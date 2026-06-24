class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            p=target-nums[i]
            if p in nums[i+1:]:
                return [i,nums[i+1:].index(p)+i+1]
        return []