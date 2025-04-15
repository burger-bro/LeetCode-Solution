from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return nums.index(max(nums))
        print("********* start **********")
        left = 0
        right = len(nums)-1 

        while left < right:
            if right - left == 1:
                left = left if nums[left] > nums[right] else right
                break
            mid = (left + right)//2
            l_mid = (left + mid)//2
            r_mid = (right + mid)//2

            idx = [left, l_mid, mid, r_mid, right]
            arr = list(map(lambda i: nums[i], idx))
            print(arr)
            tmp_max = arr.index(max(arr))
            next_map = {0: (0, 1),
                        1: (0, 2),
                        2: (1, 3),
                        3: (2, 4),
                        4: (3, 4)}
            left, right = idx[next_map[tmp_max][0]], idx[next_map[tmp_max][1]]
            print(left, right)
        ret = nums[left]
        print("ret:", ret, left)
        return left


su = Solution()

# case std1
nums = [1,2,3,1]
ans = 2
res = su.findPeakElement(nums)
assert(res == ans)

# case std2
nums = [1,2,1,3,5,6,4]
ans = 5
res = su.findPeakElement(nums)
assert(res == ans)

# case 1
nums = [1,2]
ans = 1
res = su.findPeakElement(nums)
assert(res == ans)

# case 2
nums = [2,0]
ans = 0
res = su.findPeakElement(nums)
assert(res == ans)

# case 3
nums = [2,0,1]
ans = 0
res = su.findPeakElement(nums)
assert(res == ans)

# case 
nums = [1,2,3,4,5,6,7,8,9]
ans = 8
res = su.findPeakElement(nums)
assert(res == ans)
