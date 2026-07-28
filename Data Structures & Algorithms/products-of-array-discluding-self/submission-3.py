class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix_prod = 1
        for idx, n in enumerate(nums):
            if idx == 0:
                output.append(prefix_prod)
            else :
                output.append(prefix_prod * nums[idx-1])
                prefix_prod*=nums[idx-1]

        # suffix     
        suffix=1
        for idx in range(len(nums)-1, -1, -1):
            output[idx]*=suffix
            suffix *= nums[idx]
        
        return output

            