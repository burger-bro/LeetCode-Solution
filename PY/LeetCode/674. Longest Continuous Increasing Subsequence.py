from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest_arr = [1]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                longest_arr.append(longest_arr[-1]+1)
            else:
                longest_arr.append(1)
        return max(longest_arr)



su = Solution()
nums = [1,3,5,4,7]
print(su.findLengthOfLCIS(nums))

