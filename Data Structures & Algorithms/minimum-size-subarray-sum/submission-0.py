class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        window_sum = 0
        min_len = float("inf")
        for end in range (0, len(nums)) :
            window_sum += nums[end]

            while window_sum >= target:
                len_nums = end - start + 1
                if len_nums < min_len:
                    min_len = len_nums
                window_sum-=nums[start]
                start+=1
            
        if min_len != float("inf"):
            return min_len
        else: 
            return 0
        
