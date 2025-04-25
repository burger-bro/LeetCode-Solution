from typing import List
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        m: List[bool] = [n%modulo==k for n in nums]
        # k=0需特殊处理
        print(m)
        ret = 0
        for i in range(len(m)):
            cnt = 0
            for j in range(i, len(m)):
                if m[j]:
                    cnt += 1
                if cnt % modulo == k:
                    ret += 1
        print("ret", ret)
        return ret

    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        pre = 0
        pre_map = defaultdict(int)
        count = 0
        pre_map[0] = 1
        for n in nums:
            if n % modulo == k:
                pre += 1
            rem = pre % modulo
            needed = (rem-k+modulo) % modulo
            count += pre_map[needed]
            pre_map[rem] += 1
        return count

su = Solution()
# case std1
nums = [3,2,4]
modulo = 2
k = 1
res = su.countInterestingSubarrays(nums, modulo, k)
ans = 3
assert(res == ans)
# case std2
nums = [3,1,9,6]
modulo = 3
k = 0
res = su.countInterestingSubarrays(nums, modulo, k)
ans = 2
assert(res == ans)
