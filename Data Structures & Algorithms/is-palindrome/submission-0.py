import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall(r"[a-zA-Z0-9]", s)).lower()
        l = 0
        r = len(s) - 1

        print(s)

        while l < r:
            
            if  s[l] != s[r]:
                return False

            else:
                l +=1
                r -=1

        return True 