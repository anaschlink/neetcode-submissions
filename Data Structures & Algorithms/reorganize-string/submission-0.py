from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        dic_s = Counter(s)
        heap = []
        string_s = ""
        anterior = None
        for letter, count in dic_s.items():
            heapq.heappush(heap,(-count, letter))
        
        while len(heap) !=0:
            atual = heapq.heappop(heap)
            nova_contagem = atual[0] + 1
            string_s+=atual[1]
            if anterior is not None and anterior[0] !=0:
                heapq.heappush(heap,(anterior))
                
            anterior = (nova_contagem, atual[1])

        if anterior[0] !=0:
            return ""

        return string_s
 




        
        