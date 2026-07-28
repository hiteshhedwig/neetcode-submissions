class Solution:
    def computeHours(self, piles, speed):
        totalHours = 0
        for p in piles :
            totalHours+=-(-p // speed)
        return totalHours 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while (left<=right):
            mid = left + (right - left) // 2
            rate_ = self.computeHours(piles, mid)
            if rate_ > h : 
                left=mid+1
            elif rate_ <= h:
                right=mid-1
        return left