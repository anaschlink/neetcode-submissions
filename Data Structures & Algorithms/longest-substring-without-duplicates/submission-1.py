class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest_sub = 0
        dic_s = {}
        for end in range(0,len(s)):
            if s[end] in dic_s:
                position = max(start, dic_s[s[end]] + 1)
                start = position
            dic_s[s[end]] = end
            longest_sub = max(end-start + 1, longest_sub)     
        return longest_sub

    

