class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        s, profit = prices[n - 1], 0
        for i in range(n - 2, -1, -1):
            b = prices[i]
            if b >= s:
                s = b
            else:
                if (s - b) > profit:
                    profit = s - b
        return profit
            
