from typing import List
from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 问题1如何将nums分层两个子集，并不需要，只需要找到一个子集sum=0.5总sum
        all_sum = sum(nums)
        if all_sum%2!=0: return False
        tgt_sum = all_sum/2
        glb_flag = False
        @lru_cache(None)
        def dfs(subset_sum, idx):
            nonlocal glb_flag
            if idx==len(nums): return False
            if glb_flag: return True
            if subset_sum >= tgt_sum:
                if subset_sum == tgt_sum:
                    glb_flag = True
                return False
            a1 = dfs(subset_sum+nums[idx], idx+1)
            a2 = dfs(subset_sum, idx+1)
            return a1 or a2
        dfs(0, 0)
        print(glb_flag)
        return glb_flag
        


su = Solution()
# case perf
nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
res = su.canPartition(nums)
ans = False
assert(res == ans)

# case1
nums = [i for i in range(1,201)]
res = su.canPartition(nums)
ans = True
assert(res == ans)

# case1
nums = [2]
res = su.canPartition(nums)
ans = False
assert(res == ans)

# case std1
nums = [1,5,11,5]
res = su.canPartition(nums)
ans = True
assert(res == ans)

# case std2
nums = [1,2,3,5]
res = su.canPartition(nums)
ans = False
assert(res == ans)
