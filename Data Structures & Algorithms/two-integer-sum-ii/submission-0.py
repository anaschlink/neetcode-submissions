class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while r > l:
            sum_int = (numbers[l] + numbers[r])
            if sum_int == target:
                return [l+1, r+1]
            elif sum_int < target:
                l+=1
            elif sum_int > target:
                r-=1
        return []



        