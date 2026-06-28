class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap.setdefault(n, 0)
            hashmap[n]+=1
        
        sorted_pairs = sorted(hashmap.items(), key=lambda pair: pair[1], reverse=True)
        output = []

        for m, _ in sorted_pairs[:k]:
            output.append(m)
        return output

