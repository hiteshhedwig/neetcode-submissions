class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        freqmap = {}
        maxfreq = 0
        maxlen = 0
        for right in range(len(s)):
            freqmap[s[right]]=freqmap.get(s[right],0) + 1
            maxfreq = max(maxfreq, freqmap[s[right]])
            while (right-left+1 - maxfreq) > k :
                freqmap[s[left]]-=1
                left+=1
            maxlen = max(maxlen, right-left+1)
        
        return maxlen
            
