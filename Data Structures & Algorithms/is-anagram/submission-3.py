class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        for i in s:
            hmap[i]=hmap.get(i, 0)+1
        
        for i in t:
            if i not in hmap:
                return False
            hmap[i]-=1
            if hmap[i]<0:
                return False
        
        if max(hmap.values()) >= 1:
            return False
        return True