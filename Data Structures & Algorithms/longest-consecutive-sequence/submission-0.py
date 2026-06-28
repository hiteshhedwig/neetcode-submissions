class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set()
        for n in nums :
            set_num.add(n)
        
        max_len = 0
        for n in nums:
            local_len = 0
            if n-1 not in set_num:
                i = n
                while (i in set_num) :
                    local_len += 1
                    i+=1
                max_len=max(local_len, max_len)
        return max_len
                

        