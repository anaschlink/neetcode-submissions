class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        group_start = 0
        for read in range(len(chars)):
            group_char = chars[group_start]
            if chars[read] != group_char:
                t = read - group_start
                chars[write] = chars[group_start]
                write+=1
                if t > 1: 
                    chars[write] = str(t)
                    write +=1
                group_start = read
        t = len(chars) - group_start
        chars[write] = chars[group_start]
        write+=1 
        if t > 1:
            for i in str(t):
                chars[write] = str(i)
                write+=1
        return write
        




            
        
                
        