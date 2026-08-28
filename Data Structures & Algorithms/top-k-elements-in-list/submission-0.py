class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
            
        balde = [[] for _ in range(len(nums) + 1)]

        top_k = []

        for numero, freq in nums_dict.items():
            balde[freq].append(numero)

        for top_k_list in range(len(balde) - 1, -1, -1):
            if len(top_k) < k:
                for numero in balde[top_k_list]:
                    if len(top_k) < k:
                        top_k.append(numero)

        return top_k