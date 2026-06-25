class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False

        hashmap_common = {}
        for i in s:
            if i in hashmap_common :
                hashmap_common[i]+=1
            else :
                hashmap_common[i]=1
        for i in t:
            if i in hashmap_common :
                hashmap_common[i]+=1
            else :
                return False
        
        for key,count in hashmap_common.items():
            if count%2!=0: 
                return False
        return True
        


            
        