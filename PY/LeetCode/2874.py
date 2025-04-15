from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxn, max_dff, ret = 0, 0, 0
        for n in nums:
            ret = max(ret, n*max_dff)
            maxn = max(maxn, n)
            max_dff = max(max_dff, maxn-n)
            print(maxn, max_dff, ret)
        return ret

    def maximumTripletValue(self, nums: List[int]) -> int:
        maxn, max_dff, ret = 0, 0, 0
        for n in nums:
            if n*max_dff > ret:
                ret = n*max_dff
            if n > maxn:
                maxn = n
            if maxn-n > max_dff:
                max_dff = maxn-n
        return ret

    def maximumTripletValue(self, nums: List[int]) -> int:
        maxn, max_dff, ret = 0, 0, 0
        for n in nums:
            tmp1 = n*max_dff
            if tmp1 > ret:
                ret = tmp1
            if n > maxn:
                maxn = n
            tmp2 = maxn-n
            if tmp2 > max_dff:
                max_dff = tmp2
        return ret

    def maximumTripletValue(self, nums: List[int]) -> int:
        maxn, max_dff, ret = 0, 0, 0
        for n in nums:
            tmp1 = n*max_dff
            if :
            ret = tmp1 if tmp1 > ret else ret
            if n > maxn:
                maxn = n
            tmp2 = maxn-n
            if tmp2 > max_dff:
                max_dff = tmp2
        return ret

su = Solution()
# case std1
nums = [12,6,1,2,7]
res = su.maximumTripletValue(nums)
ans = 77
assert(res == ans)
