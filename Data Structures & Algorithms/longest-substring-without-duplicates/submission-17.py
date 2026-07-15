class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check=set()
        k=0
        res=0
        for i in range(0,len(s)):
            while s[i] in check:
                check.remove(s[k])
                k+=1
            check.add(s[i])
            res=max(res,i-k+1)
        return res



            

                
                

        


            
        
            

        