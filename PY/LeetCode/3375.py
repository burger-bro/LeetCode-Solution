from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s_nums = set(nums)
        if k not in s_nums: return -1
        n_nums = list(s_nums)
        n_nums.sort()
        if n_nums[0] != k: return -1
        return len(nums)-1


