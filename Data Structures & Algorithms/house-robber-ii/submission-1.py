class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(nums: List[int]) -> int:
            len_n = len(nums)

            if len_n == 0:
                return 0

            if len_n == 1:
                return nums[0]

            prev2 = nums[0]
            prev1 = max(nums[0], nums[1])

            for i in range(2, len_n):
                current = max(prev1, nums[i] + prev2)
                prev2 = prev1
                prev1 = current

            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))