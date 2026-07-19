class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        result = 0

        while R < len(prices):
            buy = prices[L]
            sell = prices[R]

            result = max(result, sell - buy)

            if sell < buy:
                L = R
            
            R += 1

        return result

