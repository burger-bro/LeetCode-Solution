from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        cnt = 0
        left = 0
        ret = 0
        for right in range(len(nums)):
            if nums[right] == max_num:
                cnt += 1
            print(left, right)
            while cnt >= k:
                if(nums[left] == max_num):
                    cnt -= 1
                left += 1
                # ret += 1 左边的子数组
                # ret += len(nums)-1-(right+1)+1  len(nums)-right-1
                ret += len(nums)-right
            print( ret)
        print("ret", ret)        
        return ret


su = Solution()
## case std1
nums = [1,3,2,3,3]
k = 2
res = su.countSubarrays(nums, k)
ans = 6
assert(res == ans)


## case std1
nums = [1,4,2,1]
k = 3
res = su.countSubarrays(nums, k)
ans = 0
assert(res == ans)