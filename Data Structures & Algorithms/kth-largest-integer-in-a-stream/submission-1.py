class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = sorted(nums)[-k:]
        heapq.heapify(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap)<self.k : 
            heapq.heappush(self.min_heap, val)
        elif self.min_heap[0]<val:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]
