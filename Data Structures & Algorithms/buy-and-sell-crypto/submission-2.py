class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        profit = float("-inf")

        for sell in range(len(prices)):
            profit = max(prices[sell]-min_price, profit)
            if prices[sell] < min_price:
                min_price = prices[sell]
                
        
        return profit 





        



        
        