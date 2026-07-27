class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        heapq.heapify(minheap)

        for n in nums: 
            if len(minheap) < k :
                heapq.heappush(minheap, n)
            elif minheap[0] < n:
                heapq.heapreplace(minheap, n)
        
        return minheap[0]