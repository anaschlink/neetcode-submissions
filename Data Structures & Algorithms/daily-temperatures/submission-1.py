class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_index = [] 
        result = [0] * len(temperatures)
        for index, valor in enumerate(temperatures):
            while stack_index and valor > temperatures[stack_index[-1]]:
                day = stack_index[-1]
                result[day] = index - day
                stack_index.pop()
            stack_index.append(index)
        return result 

