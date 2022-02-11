class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        
        for i in range(len(prices)):
            p = prices[i] - min_price
            
            if p > max_profit:
                max_profit = p
            
            if min_price > prices[i]:
                min_price = prices[i]
        return max_profit
                
            
        
            
        