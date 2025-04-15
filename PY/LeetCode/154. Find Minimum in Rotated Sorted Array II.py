from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            if right - left == 1: return min(nums[left], nums[right])
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
            else:
                right -= 1
            print(left, right)
        return nums[left] 

su = Solution()

# case prev1
nums = [3,4,5,1,2]
ans = 1
res = su.findMin(nums)
assert(res == ans)

# case prev2
nums = [4,5,6,7,0,1,2]
ans = 0
res = su.findMin(nums)
assert(res == ans)

# case prev3
nums = [11,13,15,17]
ans = 11
res = su.findMin(nums)
assert(res == ans)

# case std1
nums = [1,3,5]
ans = 1
res = su.findMin(nums)
assert(res == ans)

# case std2
nums = [2,2,2,0,1]
ans = 0
res = su.findMin(nums)
assert(res == ans)
