class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sorted_nums = sorted(nums)
        size_nums = len(nums)
        for idx, fixed in enumerate(sorted_nums):
            if idx!=0 and sorted_nums[idx-1]==fixed:
                continue
            # twosum
            left = idx + 1
            right = size_nums - 1
            while(left<right):
                twosum = sorted_nums[left] + sorted_nums[right]
                total_sum = fixed + twosum
                if total_sum==0:
                    output.append([fixed, sorted_nums[left], sorted_nums[right]])
                    left+=1
                    right-=1
                    while(left < right and left!=0 and sorted_nums[left-1]==sorted_nums[left]):
                        left+=1
                    while(left < right and right!=(size_nums-1) and sorted_nums[right+1]==sorted_nums[right]):
                        right-=1
                if twosum<(-fixed):
                    left+=1
                if twosum>(-fixed):
                    right-=1
        
        return output
                

                

