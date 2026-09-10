class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_hash= {}
        stack = []
        result = []
        for i in range(len(nums2) -1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                    stack.pop()
            if stack:
                nums_hash[nums2[i]] = stack[-1]
            else: 
                nums_hash[nums2[i]] = -1
            stack.append(nums2[i])
        for i in nums1:
            if i in nums_hash:
                num = nums_hash[i]
                result.append(num)
        
        return result



