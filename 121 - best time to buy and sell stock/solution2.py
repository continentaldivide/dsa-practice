from __future__ import annotations

try:
    from typing import List
except:
    pass

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                    # if prices[r] - prices[l] > profit:
                    #     profit = prices[r] - prices[l]
                    temp = prices[r] - prices[l]
                    profit = max(profit, temp)
            else:
                l = r
            r += 1
        return profit

Solution().maxProfit([2,1,2,1,0,1,2])