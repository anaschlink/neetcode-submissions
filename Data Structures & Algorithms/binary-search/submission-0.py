class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:

            M = (L + R)//2
            print(M)

            if nums[M] == target:
                return M
            
            elif nums[M] < target:
                L+=1
            
            elif nums[M] > target:
                R-=1
        
        return M if nums[M] == target else -1
        


        