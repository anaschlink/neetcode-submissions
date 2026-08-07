class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        esquerda = [0] * n
        direita = [0] * n
        esquerda[0] = 1
        direita [n-1] = 1

        for i in range(1, n):
            esquerda[i] = esquerda[i-1] * nums[i-1]

        for i in range (n-2, -1, -1):
            direita[i] = direita[i+1]* nums[i+1]

        resultado = [esquerda[i] * direita[i] for i in range(n)]
        
        return resultado

        