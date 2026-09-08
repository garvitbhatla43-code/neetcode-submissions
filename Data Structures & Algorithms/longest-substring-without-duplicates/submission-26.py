class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_s = set()
        max_len = 0 
        l=0 
        for r in range(len(s)):
            while s[r] in char_s:
                char_s.remove(s[l])
                l+=1
            char_s.add(s[r])
            len1= r-l+1
            max_len = max(max_len , len1)
        return max_len
        