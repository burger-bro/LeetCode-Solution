from typing import List

class Solution:
    def __init__(self):
        self.dp = {}

    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # 注意到这个题目是要判断给定数组性质
        # 那么朴素的求解过程是：1.进行这样的分割2.判断分割后的子数组是否符合条件
        # 注意：需要排除当前数组的所有可能分割，才能判定为否
        # 方法1：dfs分解子数组，每个子数组判断是否满足性质
        # 优化点：
        # (1)维护一个sum，快速判断子数组是否符合？
        # (2)已处理过的子数组加入dp
        # (3)能否通过 已知子数组的结果 快速判断 和 子数组+1元素
        if len(nums) == 1 or len(nums) == 2: return True
        hash_key = str(nums)
        if hash_key in self.dp: return self.dp[hash_key]
        # print("nums:", nums)
        right_sum = sum(nums)
        res = False
        left_sum = 0
        for i in range(len(nums)):
            left_sum += nums[i]
            right_sum -= nums[i]
            # print(i, left_sum, right_sum)
            
            if i == 0 and right_sum >= m:
                res = self.canSplitArray(nums[i+1:], m)
            elif i == len(nums)-2 and left_sum >= m:
                res = self.canSplitArray(nums[:i+1], m)
            # elif left_sum >= m and right_sum >= m:
            #     res = self.canSplitArray(nums[:i], m) and self.canSplitArray(nums[i:], m)
            if res:
                self.dp[hash_key] = True
                return True
        # print(res)
        self.dp[hash_key] = False
        return res

    # def canSplitArray(self, nnums: List[int], m: int) -> bool:
    #     def dfs(a, b, m):
    #         nums = nnums[a:b]
    #         if len(nums) == 1 or len(nums) == 2: return True
    #         hash_key = (str(nums))
    #         if hash_key in self.dp: return self.dp[hash_key]
    #         print("nums:", nums)
    #         right_sum = sum(nums)
    #         res = False
    #         left_sum = 0
    #         for i in range(len(nums)):
    #             left_sum += nums[i]
    #             right_sum -= nums[i]
    #             print(i, left_sum, right_sum)
                
    #             if i == 0 and right_sum >= m:
    #                 res = dfs(a+i+1, b, m)
    #             elif i == len(nums)-2 and left_sum >= m:
    #                 res = dfs(a, a+i+1, m)
    #             elif left_sum >= m and right_sum >= m:
    #                 res = dfs(a, a+i, m) and dfs(a+i, b, m)
    #             if res:
    #                 self.dp[str(nums)] = True
    #                 return True
    #         print(res)
    #         self.dp[hash_key] = False
    #         return res
    #     return dfs(0, len(nums), m)
        



su = Solution()
nums = [68, 1, 78, 17, 74, 9, 50, 25, 70, 11, 100, 64, 30, 88, 9, 22, 91, 24, 89, 17, 80, 38, 12, 64, 6, 18, 61, 19, 96, 12, 98, 25, 63, 31, 10, 6, 9, 34, 83, 12, 78, 21, 40, 56, 19, 88, 9, 46, 76, 18, 79, 28, 89, 6, 44, 43, 49, 56, 53, 24, 42, 18, 50, 44, 21, 49, 41, 37, 79, 37, 26, 63, 23, 36, 54, 37, 19, 68, 35, 15, 74, 8, 6, 26, 84, 37, 24, 53, 8, 94, 11, 28, 68, 43, 49, 68, 15, 8]
m = 124
res = su.canSplitArray(nums, m)
ans = True
assert(res == ans)
exit(0)

nums = [67, 26, 100, 49, 72, 42, 38, 62, 37, 54, 35, 54, 34, 87, 23, 18, 90, 27, 55, 95, 30, 71, 65, 15, 51, 37, 70, 52, 80, 85, 63, 31, 39, 14, 31, 14, 54, 37, 45, 30, 84, 79, 29, 49, 1, 75, 46, 49, 46, 47, 82, 47, 70, 82, 31, 17, 14, 72, 65, 64, 73, 62, 46, 83, 72, 53, 76, 44, 62, 15, 21, 73, 75, 78, 39, 43, 39, 83, 89, 53, 46, 86, 63, 85, 19, 74, 98, 28, 19, 53]
m = 176
res = su.canSplitArray(nums, m)
ans = True
assert(res == ans)
exit(0)

# case 
nums = [38, 96, 25, 55, 62, 62, 58, 55, 4, 32, 35, 100, 12, 87, 16, 55, 16, 53, 77, 57, 44, 87, 23]
m = 143
res = su.canSplitArray(nums, m)
ans = False
assert(res == ans)
# exit(0)


# case bug
nums = [1, 2, 1, 1]
m = 4
res = su.canSplitArray(nums, m)
ans = False
assert(res == ans)


# case std1
nums = [2, 2, 1]
m = 4
res = su.canSplitArray(nums, m)
ans = True
assert(res == ans)

# case std2
nums = [2, 1, 3]
m = 5
res = su.canSplitArray(nums, m)
ans = False
assert(res == ans)

# case std3
nums = [2, 3, 3, 2, 3]
m = 6
res = su.canSplitArray(nums, m)
ans = True
assert(res == ans)
exit(0)