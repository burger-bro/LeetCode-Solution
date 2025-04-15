from typing import List

class Solution:
    def minCapability0(self, nums: List[int], k: int) -> int:
        ans = float("inf")
        def dfs(index, max_cap, cnt):
            nonlocal ans
            # print(index, max_cap, cnt)
            if cnt == k:
                ans = min(ans, max_cap)
                return
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                tmp_max_cap = max(max_cap, nums[i])
                dfs(i+2, tmp_max_cap, cnt+1)
        dfs(0, 0, 0)
        # print(ans)
        return ans

    def minCapability(self, nums: List[int], k: int) -> int:

        def check(m):
            cnt = 0
            i = 0
            # print("checking", mid, nums[mid])
            while i < len(nums):
                if nums[i] <= m:
                    i += 2
                    cnt += 1
                else:
                    i += 1
            # print("checking res", cnt >= k)
            return cnt >= k

        items = sorted(list(set(nums)))
        ans = float("inf")
        high = len(items)
        low = 0
        while low < high:
            mid = (high + low) // 2
            if check(items[mid]):
                ans = min(items[mid], ans)
                high = mid
            else:
                low = mid + 1
        # print(ans)
        # print(items[low])
        return ans

su = Solution()

nums = [2,3,5,9]
k = 2
ans = 5
res = su.minCapability(nums, k)
assert(ans == res)

nums = [2,7,9,3,1]
k = 2
ans = 2
res = su.minCapability(nums, k)
assert(ans == res)

nums = [2,7,9]
k = 2
ans = 9
res = su.minCapability(nums, k)
assert(ans == res)

nums = [2,7,9]
k = 1
ans = 2
res = su.minCapability(nums, k)
assert(ans == res)

nums = [999]
k = 1
ans = 999
res = su.minCapability(nums, k)
assert(ans == res)

