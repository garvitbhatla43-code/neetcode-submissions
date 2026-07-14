class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq=set(nums)
        seq=0
        for i in range(0,len(nums)):
            if nums[i]-1 not in freq:
                length=0
                while (nums[i]+length) in freq:
                    length+=1
                seq=max(length ,seq)
        return seq    