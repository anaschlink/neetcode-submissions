class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_container = 0
        p_1 = 0
        p_2 = len(heights) - 1

        while p_1 < p_2:
            container = (p_2 - p_1) * (min(heights[p_1],heights[p_2]) )
            max_container = max(max_container, container)    

            if heights[p_1] < heights[p_2]:
                p_1 +=1
            else: 
                p_2 -=1

        return max_container


        