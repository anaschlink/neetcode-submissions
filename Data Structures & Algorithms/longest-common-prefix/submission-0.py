class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs:
            min_string = min(strs, key=len)
            lenght = len(min_string)
            prefix = ""
            for i in range(lenght):
                for j in range(len(strs)):
                    if strs[j][i] != strs[0][i]:
                        return prefix
                else:   
                    prefix += strs[0][i]
            return prefix
        
        return ""
                
                

