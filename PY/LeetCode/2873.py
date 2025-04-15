from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    ret = max(ret, (nums[i] - nums[j]) * nums[k])
        return ret
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        diff_dict = {}
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                diff_dict[j] = max(nums[i]-nums[j], diff_dict.get(j, 0))
        print(diff_dict)
        max_k_dict = {}
        max_k = 0
        for k in range(n-1, -1, -1):
            max_k = max(max_k, nums[k])
            max_k_dict[k] = max_k
        print(max_k_dict)
        for i in range(1, n-1):
            ret = max(ret, max_k_dict[i+1]*diff_dict[i])
        print(ret)
        return ret

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        diff_dict = {}
        max_k_dict = {}
        max_k = 0
        for j in range(n-1, -1, -1):
            max_k = max(max_k, nums[j])
            max_k_dict[j] = max_k
            for i in range(j-1, -1, -1):
                diff_dict[j] = max(nums[i]-nums[j], diff_dict.get(j, 0))
        print(diff_dict)
        print(max_k_dict)
        ret = 0
        for i in range(1, n-1):
            ret = max(ret, max_k_dict[i+1]*diff_dict[i])
        print(ret)
        return ret


su = Solution()
nums = [12,6,1,2,7]
su.maximumTripletValue(nums)
