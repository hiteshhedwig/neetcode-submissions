class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_len = 0
        dup = set()

        for right in range(len(s)):
                while(s[right] in dup):
                    dup.remove(s[left])
                    left+=1
                dup.add(s[right])
                max_len=max(max_len, right-left+1)
        return max_len