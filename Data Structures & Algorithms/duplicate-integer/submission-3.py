class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # baseline
        # for i,_ in enumerate(nums):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
        if len(nums)<2: return False

        # optimized
        seen=set()
        i=0
        while(i<len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            i+=1
        return False
