class Solution:
    def checkRate(self, piles, k) : 
        max_p = max(piles)
        totalh = 0
        for p in piles:
            totalh += (p + k - 1) // k
        return totalh

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if self.checkRate(piles, mid) > h:
                left=mid+1
            else :
                right=mid
        return left

