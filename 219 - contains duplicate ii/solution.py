from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        for i, n in enumerate(nums):
            if n not in hash:
                hash[n] = i
            else:
                if i - hash[n] <= k:
                    return True
                else:
                    hash[n] = i
        return False