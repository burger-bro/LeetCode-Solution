from typing import List
from collections import deque

class Solution:
    # def resultsArray0(self, nums: List[int], k: int) -> List[int]:
    #     def isvalid(sub_arr):
    #         if len(sub_arr) == 1: return True
    #         last = None
    #         for i in range(len(sub_arr)):
    #             if i and sub_arr[i] - last != 1:
    #                 return False
    #             last = sub_arr[i]
    #         return True
        
    #     queue = deque([nums[i] for i in range(k)])
    #     ans = []
    #     for i in range(k-1, len(nums)):
    #         # print(nums[i], queue)
    #         if i != k-1:
    #             queue.popleft()
    #             queue.append(nums[i])
    #         ans.append(queue[-1] if isvalid(queue) else -1)
    #     # print(ans)
    #     return ans

    def resultsArray(self, nums: List[int], k: int) -> List[int]:        
        consecutive_pairs = 0
        for i in range(1, k):
            if nums[i] - nums[i-1] == 1:
                consecutive_pairs += 1

        ans = [nums[k-1] if consecutive_pairs == k - 1 else -1]

        # left, right = 0, k
        for i in range(k, len(nums)):
            if nums[i-k+1] - nums[i-k] == 1:
                consecutive_pairs -= 1
            if nums[i] - nums[i-1] == 1:
                consecutive_pairs += 1

            if consecutive_pairs == k - 1:
                ans.append(nums[i])
            else:
                ans.append(-1)

        # print(ans)
        return ans

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k==1: return nums
        ans, cnt = [], 1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                cnt+=1
            else:
                cnt = 1
            if i>=k-1:
                if cnt>=k: ans.append(nums[i])
                else: ans.append(-1)
        return ans

su = Solution()

nums = [1,2,3,4,3,2,5]
k = 3
ans = [3,4,-1,-1,-1]
res = su.resultsArray(nums, k)
assert(ans == res)

# 1num
nums = [1]
k = 1
ans = [1]
res = su.resultsArray(nums, k)
assert(ans == res)

# 2num 1k
nums = [1, 4]
k = 1
ans = [1, 4]
res = su.resultsArray(nums, k)
assert(ans == res)

# 2num 1k
nums = [1, 2]
k = 2
ans = [2]
res = su.resultsArray(nums, k)
assert(ans == res)
