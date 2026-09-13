class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l =0 
        max_len= 0
        max_f = 0
        mpp = [0]*26
        for r in range(len(s)):
            mpp[ord(s[r]) - ord("A")]+=1
            max_f = max(max_f , mpp[ord(s[r]) - ord("A")])
            while ((r-l+1) - max_f) > k:
                mpp[ord(s[l]) - ord("A")]-=1
                l+=1
                max_f = max(mpp)
            max_len = max(max_len , r-l+1)
        return max_len
        