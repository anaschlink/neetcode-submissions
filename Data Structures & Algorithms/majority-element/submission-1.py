from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        for i in nums:
            num_count[i] += 1
        
        value = max(num_count, key=num_count.get)
        return value
        