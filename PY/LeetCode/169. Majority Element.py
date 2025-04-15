from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        print(sum(nums)//len(nums))
        return max(d.keys(), key=lambda x: d[x])

    def majorityElement(self, nums: List[int]) -> int:
        s = sum(nums)//len(nums)
        max_ = max(nums)
        min_ = min(nums)
        print("debug1", sum(nums), max_*len(nums), min_*len(nums),)
        print("debug2", s, max_, min_)
        return 0

su = Solution()

nums = [3,2,3]
ans = 3
res = su.majorityElement(nums)      
# assert(res == ans)

nums = [2,2,1,1,1,2,2]
ans = 2
res = su.majorityElement(nums)        
# assert(res == ans)

nums = [2,2,1,1,1,2,2,9999]
ans = 2
res = su.majorityElement(nums)        
# assert(res == ans)
