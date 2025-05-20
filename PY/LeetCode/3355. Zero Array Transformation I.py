from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0]*len(nums)
        for l, r in queries:
            diff[l] += 1
            if r+1 < len(nums):
                diff[r+1] -= 1
        
        cur_num = 0
        for i in range(len(nums)):
            cur_num += diff[i]
            if cur_num > nums[i]:
                return False
        return True

su = Solution()
    

