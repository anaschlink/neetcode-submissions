class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in aux_dict:
                return [aux_dict[complement], i]
            aux_dict[num] = i

        