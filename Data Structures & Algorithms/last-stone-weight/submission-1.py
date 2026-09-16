import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [x *-1 for x in stones]

        heapq.heapify(heap)

        while len(heap) >=2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            x = x*-1
            y = y*-1

            if x != y:
                y = x - y 
                y = y *-1
                heapq.heappush(heap,y)
            
            if len(heap) == 0:
                return 0
        
        return (heap[0]*-1)

        