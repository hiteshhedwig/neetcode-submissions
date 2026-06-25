class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for idx, i in enumerate(nums):
        #     for j in nums[idx+1:]:
        #         if i == j:
        #             return True
        # return False

        hashmap = {}
        for i in nums:
            if i in hashmap :
                hashmap[i]+=1
            else :
                hashmap[i]=1
            if hashmap[i]>1:
                return True
        return False
        