class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = list(s)
        maxS = 1
        if len(s) == 0:
            return 0
        for i, j in enumerate(l):
            ts = set()
            ts.add(j)
            for k, n in enumerate(l[i + 1:]):
                badd = len(ts)
                ts.add(n)
                aadd = len(ts)
                if badd == aadd:
                    if maxS < badd:
                        maxS = badd
                    break
                if maxS < aadd:
                    maxS = aadd

        return maxS
