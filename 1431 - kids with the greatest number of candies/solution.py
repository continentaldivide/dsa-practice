from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = 0
        bools = []
        for c in candies:
            if c > highest:
                highest = c
        cutoff = highest - extraCandies
        for c in candies:
            if c >= cutoff:
                bools.append(True)
            else:
                bools.append(False)
        return bools
    
print(Solution().kidsWithCandies([2,3,5,1,3], 3))