class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False
        win_len=len(s1)
        left=0
        hashmap_s1 = {}
        for i in range(win_len):
            hashmap_s1[s1[i]]=hashmap_s1.get(s1[i], 0) + 1
        
        hashmap_sub={}
        for right in range(len(s2)):
            hashmap_sub[s2[right]] = hashmap_sub.get(s2[right],0)+1
            
            while right-left+1 > win_len:
                hashmap_sub[s2[left]]-=1
                if hashmap_sub[s2[left]]<=0:
                    hashmap_sub.pop(s2[left])
                left+=1
                    
            if right-left+1==win_len:
                if hashmap_sub==hashmap_s1:
                    return True
        
        return False
