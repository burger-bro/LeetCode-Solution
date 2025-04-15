from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxn = nums[0]
        minn = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxn, minn = minn, maxn
            maxn = max(maxn * nums[i], maxn)
            minn = min(minn * nums[i], minn)
        return max(maxn, minn)
            

s = Solution()
# nums = [2,3,-2,4]
# assert(s.maxProduct(nums) == 6)

# nums = [-2,0,-1]
# assert(s.maxProduct(nums) == 0)

# nums = [-2,]
# assert(s.maxProduct(nums) == -2)

nums = [-2,3,-4]
assert(s.maxProduct(nums) == 24)
