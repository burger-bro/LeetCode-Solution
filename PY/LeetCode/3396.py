from typing import List
from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = Counter(nums)
        distinct_n = set()
        for k, v in d.items():
            if v!=1:
                distinct_n.add(k)
        length = len(nums)
        idx = 0
        cnt = 0
        while idx<length:
            if not distinct_n: break
            max_elem = min(3, length-idx)
            for i in range(idx,idx+max_elem):
                d[nums[i]] -= 1
                if d[nums[i]] == 1:
                    distinct_n.discard(nums[i])
            cnt += 1
            idx += max_elem
        print(cnt)
        return cnt

su = Solution()

# case std1
nums = [1,2,3,4,2,3,3,5,7]
res = su.minimumOperations(nums)
ans = 2
assert(res == ans)

# case std2
nums = [4,5,6,4,4]
res = su.minimumOperations(nums)
ans = 2
assert(res == ans)
