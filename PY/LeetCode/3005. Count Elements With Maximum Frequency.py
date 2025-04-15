from typing import List
from collections import Counter, defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = Counter(nums)
        max_f = max(d.values())
        total = 0
        for k, v in d.items():
            if v == max_f:
                total += v
        return total

    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)

        max_f = 0
        max_cnt = 0
        for n in nums:
            d[n] += 1
            if d[n] > max_f:
                max_f = d[n]
                max_cnt = 1
            elif d[n] == max_f:
                max_cnt += 1

        return max_f * max_cnt

su = Solution()
a = [1,1,2,2,3,3,4,5,6]
print(su.maxFrequencyElements(a))
# 11 4 C
# a  b 70
# a + b = 110
# a = 110*11/15 b = 110*4/15

# 40  x    y
#  9  14   11