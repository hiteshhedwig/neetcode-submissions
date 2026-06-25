class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in hashmap:
                hashmap[ss] = []
                hashmap[ss].append(s)
            else :
                hashmap[ss].append(s)

        output = []
        for _, val in hashmap.items():
            output.append(val)
        return output