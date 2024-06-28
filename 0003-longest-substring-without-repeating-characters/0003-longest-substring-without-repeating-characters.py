class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        max_l = 0
        local_word_start = 0
        for index, c in enumerate(s):
            if c in m and m[c] >= local_word_start:
                local_word_start = m[c] + 1
            local_max = index - local_word_start + 1
            max_l = max(max_l, local_max)
            m[c] = index
        

        return max_l
        