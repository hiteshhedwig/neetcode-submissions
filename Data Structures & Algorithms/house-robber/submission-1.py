class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     len_n = len(nums)
    #     dp = [0]*len_n

    #     dp[0] = nums[0]
    #     dp[1] = nums[1]

    #     for i in range(2, len_n):
    #         dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        
    #     return dp[-1]

    def rob(self, nums: List[int]) -> int:
        len_n = len(nums)
        if len_n == 1:
            return nums[0]
            
        prev2 = nums[0]
        prev1 = max(nums[1], nums[0])

        for i in range(2, len_n):
            current = max(prev1, nums[i]+prev2)
            prev2=prev1
            prev1=current

        return prev1