class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        prev={}
        for i in range(0,len(nums)):
            if nums[i] in prev:
                prev[nums[i]]+=1
            else:
                prev[nums[i]]=1
        sorted_pairs = sorted(prev.items(), key=lambda x: x[1])
        sorted_hash_map = dict(sorted_pairs)
        all_keys=list(sorted_hash_map.keys())
        kth_return=all_keys[-k:]
        return kth_return
    
                