from typing import List
from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        pos_b = [0]*len(nums2)
        for idx, n in enumerate(nums2):
            pos_b[n] = idx

        pre_a, pos_in_b = [0], SortedList([pos_b[nums1[0]]])
        for n in nums1[1:]:
            pos_in_b.add(pos_b[n])
            pre_a.append(pos_in_b.bisect_left(pos_b[n]))

        suf_a, pos_in_b = [0], SortedList([pos_b[nums1[-1]]])
        for n in (nums1[:-1])[::-1]:
            pos_in_b.add(pos_b[n])
            idx = pos_in_b.bisect(pos_b[n])
            suf_a.append(len(pos_in_b)-idx)
        suf_a.reverse()

        ret = 0
        for i in range(len(pre_a)):
            ret += pre_a[i]*suf_a[i]
        print(ret)
        return ret
        

su = Solution()
# case std1
nums1 = [2,0,1,3]
nums2 = [0,1,2,3]
res = su.goodTriplets(nums1, nums2)
ans = 1
assert(res == ans)
# case std2
nums1 = [4,0,1,3,2]
nums2 = [4,1,0,2,3]
res = su.goodTriplets(nums1, nums2)
ans = 4
assert(res == ans)
