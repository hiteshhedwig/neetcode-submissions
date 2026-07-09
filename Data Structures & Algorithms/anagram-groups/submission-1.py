class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for idx, n in enumerate(strs):
            sn="".join(sorted(n))
            if sn in hmap:
                hmap[sn].append(n)
            else :
                hmap[sn]=[n]
        
        output=[]
        for k,v in hmap.items():
            output.append(v)
        return output
