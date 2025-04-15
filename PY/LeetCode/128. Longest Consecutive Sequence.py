from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        longest = 0
        ret = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                longest += 1
                ret = max(longest, ret)
            elif nums[i] - nums[i-1] == 0:
                continue
            else:
                longest = 0
        print("ret:", ret+1)
        return ret+1

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     # 0, 1, 2, 3, 4
    #     # 4, 3, 2, 1, 0
    #     # 0, 1, 5, 2, 3
    #     # 遍历方式：从前往后
    #     # 当读取完第一个值后，可用作参考的量为？last、min、max
    #     # 读取一个值后，假设有序，并追踪当前有序段的max和min，之后每一个值都和这两个值比较。
    #     # 如果后续值不再有序了该怎么处理？再创建一个新的有序段，后续值进行类似判断。
    #     ret = 0
    #     consecutive_dict_begin = {nums[0]: nums[0]}
    #     consecutive_dict_end = {nums[0]: nums[0]}
    #     for n in nums[1:]:
    #         if n-1 in consecutive_dict_end:
    #             consecutive_dict_end[n] = consecutive_dict_end[n-1]
    #             consecutive_dict_begin[consecutive_dict_end[n-1]] = n
    #             ret = max(ret, abs(consecutive_dict_end[n] - n))
    #         elif n+1 in consecutive_dict_begin:
    #             consecutive_dict_begin[n] = consecutive_dict_begin[n+1]
    #             consecutive_dict_end[consecutive_dict_begin[n+1]] = n
    #             ret = max(ret, abs(n - consecutive_dict_begin[n]))
    #         else:
    #             consecutive_dict_begin[n] = n
    #             consecutive_dict_end[n] = n
    #         print("b", consecutive_dict_begin)
    #         print("e", consecutive_dict_end)
    #     print(ret)
    #     return ret+1

    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        nums_set = set(nums)
        for n in nums:
            if n -1 not in nums_set:
                length = 1
                while n+length in nums_set:
                    length += 1
                longest = max(longest, length)
        print(longest)
        return longest

su = Solution()
# case std1
nums = [100,4,200,1,3,2]
res = su.longestConsecutive(nums)
ans =  4
assert(res == ans)
# case std2
nums = [0,3,7,2,5,8,4,6,0,1]
res = su.longestConsecutive(nums)
ans = 9
assert(res == ans)
# case1 len0
nums = [2]
res = su.longestConsecutive(nums)
ans = 1
assert(res == ans)
# case2 len1
nums = [2,0]
res = su.longestConsecutive(nums)
ans = 1
assert(res == ans)
# case3 len2
nums = [2,0,1]
res = su.longestConsecutive(nums)
ans = 3
assert(res == ans)
# case4
nums = []
res = su.longestConsecutive(nums)
ans = 0
assert(res == ans)
# case5
nums = [0,1,2,1]
res = su.longestConsecutive(nums)
ans = 3
assert(res == ans)