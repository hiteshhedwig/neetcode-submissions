class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        size_n = len(nums)

        prefix_arr = [1] * size_n
        prefix_mul = 1
        for i in range(size_n):
            prefix_arr[i] = prefix_mul
            prefix_mul *= nums[i]
        
        suffix_arr = [1] * size_n
        suffix_mul = 1
        for i in range(size_n):
            s_i = size_n - i - 1
            suffix_arr[s_i] = suffix_mul
            suffix_mul *= nums[s_i]   

        output = []
        for i in range(len(prefix_arr)):
            output.append(prefix_arr[i] * suffix_arr[i])
        
        return output
        