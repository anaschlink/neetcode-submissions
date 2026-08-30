class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest= 0
        window_char = {}
        for end in range(0, len(s)):
            if s[end] in window_char:
                window_char[s[end]] += 1
            else: 
                window_char[s[end]] = 1

            while window_char[s[end]] > 1:
                window_char[s[start]] -= 1 
                start+=1

            longest = max(end - start + 1, longest)
        return longest 
        
         

