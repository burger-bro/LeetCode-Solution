# 1, 6, 1, 5, 1, 4
from collections import deque

class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = nums.copy()
        print(arr)
        arr.sort()
        print(arr)
        nums.clear()
        i = 0
        j = len(arr) // 2
        res = deque()
        while i < len(arr) // 2:
            res.append(arr[i])
            res.append(arr[j])
            i += 1
            j += 1
        if len(res) != len(arr):
            res.append(arr[i])
        print(res)

su = Solution()
# nums = [1,5,1,1,6,4,7]
# assert su.wiggleSort(nums) == [1,6,1,5,1,4]

nums = [1,1,2,1,2,2,1]
assert su.wiggleSort(nums) == [1,2,1,2,1,2,1]
