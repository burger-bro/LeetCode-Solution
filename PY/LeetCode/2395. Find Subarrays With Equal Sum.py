from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)-1):
            sum = nums[i] + nums[i+1]
            if sum in d and i not in d[sum]:
                return True
            d[sum] = d.get(sum, set())
            d[sum].add(i)
        print(d)
        return False

    def findSubarrays(self, nums: List[int]) -> bool:
        d = set()
        for i in range(len(nums)-1):
            sums = nums[i] + nums[i+1]
            if sums not in d:
                d.add(sums)
            else:
                return True
        return False

su = Solution()

# case1
nums = [0,1]
res = su.findSubarrays(nums)
ans = False
assert(res == ans)

# case std1
nums = [4,2,4]
res = su.findSubarrays(nums)
ans = True
assert(res == ans)

# case std2
nums = [1,2,3,4,5]
res = su.findSubarrays(nums)
ans = False
assert(res == ans)

# case std3
nums = [0,0,0]
res = su.findSubarrays(nums)
ans = True
assert(res == ans)
