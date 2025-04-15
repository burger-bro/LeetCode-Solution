from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        if right == 0:
            return nums[0]
        elif right == 1:
            return min(nums)
        mid = right // 2
        left = 0
        while left < right:
            if right - left == 1:
                return nums[right]
            if nums[left] < nums[mid] < nums[right]:
                return nums[0]
            print("b l:%d m:%d r:%d" % (left, mid, right))
            if nums[left] > nums[mid]:
                right = mid
            if nums[mid] > nums[right]:
                left = mid
            mid = (left + right) // 2
            print("a l:%d m:%d r:%d" % (left, mid, right))
        print("res:", nums[mid + 1])
        return nums[mid + 1]



s = Solution()


nums = [3,4,5,1,2]
res1 = 1
assert(s.findMin(nums) == res1)

nums = [4,5,6,7,0,1,2]
res2 = 0
assert(s.findMin(nums) == res2)

nums = [11,13,15,17]
res3 = 11
assert(s.findMin(nums) == res3)

nums = [11]
res4 = 11
assert(s.findMin(nums) == res4)

nums = [2, 3, 1]
res5 = 1
assert(s.findMin(nums) == res5)

nums = [4,5,1,2,3]
res6 = 1
assert(s.findMin(nums) == res6)
