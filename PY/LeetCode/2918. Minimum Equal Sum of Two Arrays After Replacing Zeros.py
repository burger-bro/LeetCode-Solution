from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2, zero1, zero2 = 0, 0, 0, 0
        for n in nums1:
            sum1 += n
            if n == 0: 
                zero1 += 1

        for n in nums2:
            sum2 += n
            if n == 0: 
                zero2 += 1
        
        if zero1 != 0 and zero2 != 0:
            return max(zero1+sum1, zero2+sum2)
        elif zero1 == 0 and zero2 == 0:
            if sum1 == sum2: 
                return sum1
            else:
                return -1
        elif zero1 == 0:
            if sum1 < sum2+zero2: return -1
            return sum1
        elif zero2 == 0:
            if sum2 < sum1+zero1: return -1
            return sum2

su = Solution()
# case1
nums1 = [3,2,0,1,0]
nums2 = [6,5,0]
res = su.minSum(nums1, nums2)
print("res: ", res)
ans = 12
assert(res == ans)
# case2
nums1 = [2,0,2,0]
nums2 = [1,4]
res = su.minSum(nums1, nums2)
print("res: ", res)
ans = -1
assert(res == ans)
# case3
nums1 = [2,2,2]
nums2 = [1,4]
res = su.minSum(nums1, nums2)
print("res: ", res)
ans = -1
assert(res == ans)
