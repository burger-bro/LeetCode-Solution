from typing import List

class Solution:
    def countAlternatingSubarrays0(self, nums: List[int]) -> int:
        dp = [[-1] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = 1
        def recursive(start, end):
            if start == end: return True

            flag = False
            if start + 1 <= end:
                res = dp[start+1][end] == 1 or recursive(start+1, end)
                # res = recursive(start+1, end)
                if res and nums[start+1] + nums[start] == 1:
                    dp[start][end] = 1
                    flag = True

            if start <= end - 1:
                # res = dp[start][end-1] == 1 or recursive(start, end-1)
                res = recursive(start, end-1)
                if res and nums[end] + nums[end-1] == 1:
                    dp[start][end] = 1
                    flag = True
            
            return flag

        recursive(0, len(nums)-1)
        # print(dp)
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if dp[i][j] == 1:
                    ans += 1
        return ans

    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        # dp[0] = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                dp[i] = dp[i-1] + 1

        # print(dp)
        # print(sum(dp))
        return sum(dp)


su = Solution()

nums = [0,1,1,1]
ans = 5
res = su.countAlternatingSubarrays(nums)
assert(ans == res)

nums = [1,0,1,0]
ans = 10
res = su.countAlternatingSubarrays(nums)
assert(ans == res)

nums = [1]
ans = 1
res = su.countAlternatingSubarrays(nums)
assert(ans == res)

nums = [1,1]
ans = 2
res = su.countAlternatingSubarrays(nums)
assert(ans == res)

nums = [1,1,1,1,1]
ans = 5
res = su.countAlternatingSubarrays(nums)
assert(ans == res)

nums = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0]
ans = 5
res = su.countAlternatingSubarrays(nums)
# assert(ans == res)

