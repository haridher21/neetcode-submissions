class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        s, profit = 0, 0
        for i in range(n - 1, -1, -1):
            b = prices[i]
            if b < s:
                if (s - b) > profit:
                    profit = s - b
            else:
                s = b
        return profit
            
