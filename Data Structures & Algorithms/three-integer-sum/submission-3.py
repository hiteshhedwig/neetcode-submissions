class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0: return []
        
        nums.sort()

        output=[]
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            # apply 2sum
            left=i+1
            right=len(nums)-1
            while (left<right) :
                threesum = nums[i] + nums[left] + nums[right]
                if threesum == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    # now this is recorded, we move left and right inwards
                    while (left < right and nums[left]==nums[left-1]):
                        left+=1
                    while (left < right and nums[right]==nums[right+1]):
                        right-=1
            
                if threesum>0:
                    # i make right pointer move inwards!
                    right-=1
                if threesum<0:
                    # i make left pointer move towards middle of the array
                    left+=1
        
        return output


                


