from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ret = 0
        for i in range(len(nums)):
            tmp_sum = 0
            for j in range(i, len(nums)):
                tmp_sum += nums[j]
                if (j-i+1) * tmp_sum < k:
                    ret += 1
                else:
                    break
        print("Ret", ret)
        return ret
    
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ret = 0
        for start in range(len(nums)):
            left, right = start, len(nums)-1
            find = -1
            while left <= right:
                mid = left + (right - left)//2
                if sum(nums[start:mid+1])*(mid-start+1) < k:
                    find = mid
                    left = mid+1
                else:
                    right = mid-1
            ret += 0 if find == -1 else find-start+1
        return ret
    
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ret = 0
        for start in range(len(nums)):
            left, right = start, len(nums)-1
            find = -1
            tmp_sum = -1
            flag = "no"

            while left <= right:
                mid = left + (right - left)//2
                    
                if tmp_sum == -1:
                    tmp_sum = sum(nums[start:mid+1])*(mid-start+1)
                else:
                    if flag == "add":
                        tmp_sum = (tmp_sum // (left-start) + sum(nums[left+1:mid+1])) * (mid-start+1)
                    elif flag == "sub":
                        tmp_sum = (tmp_sum // (right+1-start+1) - sum(nums[mid+1:right+1])) * (mid-start+1)
                if tmp_sum < k: # sum(nums[start:mid+1])*(mid-start+1) < k:
                    find = mid   
                    left = mid+1 
                    flag = "add"
                else:
                    right = mid-1
                    flag = "sub"

            ret += 0 if find == -1 else find-start+1
        return ret

    def countSubarrays(self, nums: List[int], k: int) -> int:
        tmp_sum, res, j = 0, 0, 0
        for i, n in enumerate(nums):
            tmp_sum += n
            while tmp_sum * (i- j + 1) >= k:
                tmp_sum -= nums[j]
                j += 1
            res += i - j + 1
        return res

su = Solution()
# case perf
nums = [i for i in range(1, 50000)]
k = 100000000
res = su.countSubarrays(nums, k)
ans = 6

# case std1
nums = [2,1,4,3,5]
k = 10
res = su.countSubarrays(nums, k)
ans = 6
assert(res == ans)

# case std2
nums = [1,1,1]
k = 5
res = su.countSubarrays(nums, k)
ans = 5
assert(res == ans)
