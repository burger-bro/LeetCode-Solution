from typing import List
from collections import defaultdict
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        nums.sort()
        last = nums[0]
        ans = -float("inf")
        for n in nums[1:]:
            ans = max(n-last, ans)
            last = n
        print(ans)
        return ans

    def maximumGap(self, nums: List[int]) -> int:
        # nums.sort()
        # ss = 0
        # for i in range(1, len(nums)):
        #     ss += nums[i] - nums[i-1]
        # print(ss)
        bucket_size = len(nums) - 1
        max_v = max(nums)
        min_v = min(nums)
        length = max_v - min_v
        buckets = {}
        for n in nums:
            idx = int(((n - min_v) / length) * bucket_size)
            if idx not in buckets:
                buckets[idx] = (n, n)
            else:
                prev_max, prev_min = buckets[idx][0], buckets[idx][1]
                buckets[idx] = (max(prev_max, n), min(prev_min, n))
        print(buckets)
        idxs = sorted(buckets.keys())
        prev_max = buckets[idxs[0]][0]
        result = 0
        for idx in idxs:
            result = max(result, buckets[idx][1]-prev_max)
            prev_max = buckets[idx][0]
        print(result)
        return result

    def maximumGap(self, nums):
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo: return hi - lo
        B = defaultdict(list)
        for num in nums:
            ind = n-2 if num == hi else (num - lo)*(n-1)//(hi-lo)
            B[ind].append(num)
            
        cands = [[min(B[i]), max(B[i])] for i in range(n-1) if B[i]]
        tmp = zip(cands, cands[1:])
        print(tmp)
        print(cands)
        for h in tmp:
            print(h)
        return max(y[0]-x[1] for x,y in zip(cands, cands[1:]))

su = Solution()
# case debug
nums = [3,14,15,83,6,4,19,20,40]
# nums = [1,10000000]
res = su.maximumGap(nums)
exit(0)

# case 1
nums = [3,10,2,8,6,9,1]
ans = 3
res = su.maximumGap(nums)

# case std1
nums = [3,6,9,1]
ans = 3
res = su.maximumGap(nums)

# case std2
nums = [10]
ans = 0
res = su.maximumGap(nums)
assert(res == ans)
