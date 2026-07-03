class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in range(0,len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        sorted_pairs=sorted(freq.items(),key=lambda x: x[1])
        hash_map=dict(sorted_pairs)
        all_keys=list(hash_map.keys())
        return all_keys[-k:]