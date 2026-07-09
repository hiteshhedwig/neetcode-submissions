class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        bucket = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            hmap[n]=hmap.get(n, 0) + 1
        
        # build bucket
        for key, v in hmap.items():
            bucket[v].append(key)
        
        out=[]
        req=k
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                out.append(j)
                req-=1
                if req==0:
                    return out
        
        return out
