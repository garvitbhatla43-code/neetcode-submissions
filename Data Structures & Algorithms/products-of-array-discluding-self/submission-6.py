class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prifix=[1]*len(nums)
        suffix=[1]*len(nums)
        output=[1]*len(nums)
        for i in range(1,len(nums)):
            prifix[i]=prifix[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        for i in range(len(nums)):
            output[i]=prifix[i]*suffix[i]
        return output 
        