from collections import Counter
from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def count(one, two):
            d = Counter(one)
            print(d)
            maxK, maxV = None, -1
            for k, v in d.items():
                if v > maxV:
                    maxV = v
                    maxK = k
            print(maxK)
            for i in range(len(one)):
                if one[i] != maxK and two[i] != maxK:
                    return float("inf")
            return len(one)-maxV

        res1 = count(tops, bottoms)
        res2 = count(bottoms, tops)
        print(res1, res2)
        res = min(res1, res2)
        return -1 if res == float("inf") else res

su = Solution()
tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
res = su.minDominoRotations(tops, bottoms)
ans = 2
assert(res == ans)

tops = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
res = su.minDominoRotations(tops, bottoms)
ans = -1
assert(res == ans)
