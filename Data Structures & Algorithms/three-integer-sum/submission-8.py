class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        limite = len(nums) - 3
        result = []

        nums_ord = sorted(nums)

        while i <= limite:

            if i > 0 and nums_ord[i] == nums_ord[i - 1]:
                i += 1
                continue

            j = i + 1
            k = len(nums_ord) -1

            while j < k:

                total = nums_ord[i] + nums_ord[j] + nums_ord[k]

                if (total) == 0:
                    result.append([nums_ord[i] , nums_ord[j], nums_ord[k]])
                    k -=1
                    j+=1

                    while j < k and nums_ord[j] == nums_ord[j - 1]:
                        j += 1

                    while j < k and nums_ord[k] == nums_ord[k + 1]:
                        k -= 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1
                
            i+=1

        return result


        

        