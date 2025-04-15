from typing import List
from itertools import combinations
from functools import reduce

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ret = 0
        for i in range(1, len(nums)+1):
            for c in combinations(nums, i):
                ret += reduce(lambda a, b: a^b, c)
        return ret

    def subsetXORSum(self, nums: List[int]) -> int:
        return sum(reduce(lambda a, b: a^b, c) for i in range(1, len(nums)+1) for c in combinations(nums, i))

    # def subsetXORSum(self, nums: List[int]) -> int:
    #     # C(nums, 2)

su = Solution()

# case std1
nums = [1]
res = su.subsetXORSum(nums)    
ans = 1
assert(res == ans)


# case std1
nums = [1,3]
res = su.subsetXORSum(nums)    
ans = 6
assert(res == ans)

# case std2
nums = [5,1,6]
res = su.subsetXORSum(nums)    
ans = 28
assert(res == ans)