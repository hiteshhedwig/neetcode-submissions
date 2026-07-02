class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        freq_map = {}
        max_freq = 0
        max_len = 0
        
        while(right<len(s)):
            freq_map[s[right]] = freq_map.setdefault(s[right], 0) + 1
            max_freq = max(freq_map[s[right]] , max_freq)
            while ((right - left + 1)- max_freq) > k :
                freq_map[s[left]] -= 1
                if freq_map[s[left]] == 0:
                    freq_map.pop(s[left])
                left += 1
                max_freq = max(freq_map.values(), default=0)
            max_len = max(max_len, right - left + 1)
            right+=1
        return max_len
            