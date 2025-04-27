from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ret = 0
        for i in range(len(nums)):
            cur_min, cur_max = nums[i], nums[i]
            for j in range(i, len(nums)):
                cur_max = max(cur_max, nums[j])
                cur_min = min(cur_min, nums[j])
                if cur_max == maxK and cur_min == minK:
                    ret += 1

        print("ret: " ,ret)
        return ret

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ret = 0
        for i in range(len(nums)):
            cur_min, cur_max = nums[i], nums[i]
            for j in range(i, len(nums)):
                cur_max = max(cur_max, nums[j])
                cur_min = min(cur_min, nums[j])
                if cur_max == maxK and cur_min == minK:
                    ret += 1
                elif cur_max > maxK or cur_min < minK:
                    break

        return ret

    def countSubarrays(self, nums: List[int], minK: int, maxK: int):
        """
        使用双指针的思路：
        当前节点不超过minK和maxK继续 否则终止 查看之前遍历结果是否有符合
        遍历过程中 两个bool值记录 是否有mink和maxk
        难点 对于满足性质的这样一个子数组 若里面有多对mink和maxk则还有子答案

        
        直接计数的思路：
        找到所有的minK和maxK 并且按大于maxK和小于minK的值分组
        对于每一个分组有一个minK分组和一个maxK分组
        可以求minK分组和maxK分组的全组合 
        对于每一个(minK, maxK)组合 合法的subarray就是 mink maxk到他们之外另一值的乘积
        """
        def deal_subarray(sub_array):
            sub_arrs = []
            last = 0
            cur_max = sub_array[0]
            cur_min = sub_array[0]
            for i in range(len(sub_array)):
                cur_max = max(cur_max, nums[i])
                cur_min = min(cur_min, nums[i])
                if cur_max > maxK or cur_min < minK:
                    if i != 0: # 不加也可以，空数组
                        sub_arrs.append((last, i))
                    cur_max = -float("inf")
                    cur_min = float("inf")
                    last = i+1
            print(sub_arrs)
        deal_subarray(nums)

su = Solution()
# case std1
nums = [1,3,5,2,7,5]
minK = 1
maxK = 5
res = su.countSubarrays(nums, minK, maxK)
ans = 2 
assert(res == ans)
# case std2
nums = [1,1,1,1]
minK = 1
maxK = 1
res = su.countSubarrays(nums, minK, maxK)
ans = 10
assert(res == ans)

