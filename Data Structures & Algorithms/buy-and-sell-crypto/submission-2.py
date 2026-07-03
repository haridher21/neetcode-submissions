class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s, profit = 0, 0
        for i in range(len(prices) - 1, -1, -1):
            b = prices[i]
            if b < s:
                if (s - b) > profit:
                    profit = s - b
            else:
                s = b
        return profit
            
