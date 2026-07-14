class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq=set(nums)
        seq=0

        for i in nums:
            if (i-1) not in freq:
                length=0
                while (i+length) in freq:
                    length+=1
                seq=max(length,seq)
        return seq
                