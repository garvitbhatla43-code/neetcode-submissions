class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        chars= set()
        for i in range(0,len(s)):
            while s[i] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[i])
            res= max(res, i-l+1)
        return res 
        

        