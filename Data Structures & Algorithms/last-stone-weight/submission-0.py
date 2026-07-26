class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap =  [-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            f_ele = -1*heapq.heappop(maxheap)
            s_ele = -1*heapq.heappop(maxheap)

            if f_ele==s_ele:
                continue
            diff = (f_ele-s_ele)
            heapq.heappush(maxheap, -1*diff)

        return 0 if len(maxheap)==0 else -1*maxheap[0]

