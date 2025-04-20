from typing import List

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        """
        如何证明？
        """
        last_seen = -1
        i = 0
        cnt = 0
        while i < len(nums):
            if nums[i] >= last_seen:
                print("i:", i, nums[i])
                last_seen = nums[i]
                cnt += 1
            i += 1
        print("cnt", cnt)
        return cnt

su = Solution()
# case std1
nums = [4,2,5,3,5]
res = su.maximumPossibleSize(nums)
ans = 3
assert(res == ans)

# case std2
nums = [1,2,3]
res = su.maximumPossibleSize(nums)
ans = 3
assert(res == ans)
