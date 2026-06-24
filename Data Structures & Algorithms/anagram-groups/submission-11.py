class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        popl=defaultdict(list)
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord("a")]+=1

            popl[tuple(count)].append(i)
        return list(popl.values())