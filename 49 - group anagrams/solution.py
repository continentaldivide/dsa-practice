from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        list = []
        for str in strs:
            # first try commented out...

            # for prop in dict:
            #     if self.singleAnagram(str, dict[prop][0]):
            #         dict[prop].append(str)
            #         canary = True
            # if not canary:
            #     dict[str] = [str]

            # looks like the solution above gets into O(n^2) territory and takes too long.  instead of iterating over dict -- what if we alphabetize the str, then check for a prop in dict with that name?  if not, add prop and append str.  if found, append str.  skips iterating over dict but adds sort time

            alpha = ''.join(sorted(str))
            if alpha not in dict:
                dict[alpha] = [str]
            else:
                dict[alpha].append(str)

            # it works!

        for prop in dict:
            list.append(dict[prop])
        return(list)

    def singleAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for c in s:
            if c not in s_hash:
                s_hash[c] = 1
            else:
                s_hash[c] += 1
        for c in t:
            if c not in t_hash:
                t_hash[c] = 1
            else:
                t_hash[c] += 1
        return s_hash == t_hash

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))