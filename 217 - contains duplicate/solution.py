from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for n in nums:
            if n not in hash:
                hash[n] = True
            else:
                return True
        return False