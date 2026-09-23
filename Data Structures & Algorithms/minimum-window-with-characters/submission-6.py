class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l =0 
        r= 0
        count = 0
        start_idx = -1 
        min_len = 10**9
        hash_m = [0]*256
        m=len(t)
        n=len(s)
        for i in range(0,m):
            hash_m[ord(t[i])]+=1
        while r<n:
            if hash_m[ord(s[r])] > 0:
                count+=1
            hash_m[ord(s[r])] -=1 
            while count == m:
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    start_idx = l
                hash_m[ord(s[l])]+=1
                if hash_m[ord(s[l])] > 0:
                    count-=1
                l+=1
            r+=1
        if start_idx == -1:
            return ""
        else: 
            return s[start_idx : start_idx+min_len]



        