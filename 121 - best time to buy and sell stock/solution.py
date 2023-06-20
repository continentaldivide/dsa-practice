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
        for p in prices:
            print(l, r)
            if r < len(prices):
                if p < prices[l]:
                    l = prices.index(p)
                if prices[l] > prices[r]:
                    l, r = l + 1, r + 1
                else:
                    if prices[r] - prices[l] > profit:
                        profit = prices[r] - prices[l]
                    r += 1
            print(profit)
        return profit

Solution().maxProfit([2,1,2,1,0,1,2])