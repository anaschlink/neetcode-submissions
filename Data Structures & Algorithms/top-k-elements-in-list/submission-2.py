from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic_element = Counter(nums)
        heap = []
        result = []

        for value, count in dic_element.items():
            heapq.heappush(heap,(-count, value))

        for top_k in range(k):
            element = heapq.heappop(heap)
            result.append(element[1])
        
        return result