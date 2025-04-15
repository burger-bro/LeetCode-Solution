from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """
        注意到非降序：
        所以当遇到形如x[i]<=x[i+1]的pair时 可直接跳过 否则
        (1)用x[i]吸收后面的值 一定是最优吗？
        (2)想办法合并x[i+1]和它之后的值使得x[i]<=merge(x[i+1]+x[i+1+t])
        5 2 3 1


        单调栈？
        """
        stack = []
        cnt = len(nums)-1
        ret = 0
        while cnt >= 0:
            if not stack:
                stack.append(nums[cnt])
            else:
                while stack[-1] < nums[cnt] or (len(stack) >= 2 and stack[-1]>stack[-2]):
                    if len(stack) == 1: break
                    ret += 1
                    tmp = stack.pop()
                    stack[-1] += tmp
                if stack[-1] >= nums[cnt]:
                    stack.append(nums[cnt])
                else:
                    ret += 1
                    stack[-1] += nums[cnt]
            print("cur:", nums[cnt], ret)
            cnt -= 1
            print("stack:", stack)
        print(ret)
        return ret
    
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """
        注意到非降序：
        所以当遇到形如x[i]<=x[i+1]的pair时 可直接跳过 否则
        (1)用x[i]吸收后面的值 一定是最优吗？
        (2)想办法合并x[i+1]和它之后的值使得x[i]<=merge(x[i+1]+x[i+1+t])
        5 2 3 1

        单调栈？
        """
        def is_sorted(nums):
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    return False
            return True
        
        ret = 0
        while not is_sorted(nums):
            min_idx = 0
            min_sum = float("inf")
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1] < min_sum:
                    min_sum = nums[i]+nums[i+1] 
                    min_idx = i
            nums = nums[:min_idx]+[min_sum]+nums[min_idx+2:]
            ret += 1
        print(ret)
        return ret


su = Solution()
# case bug
nums = [-2,1,2,-1,-1,-2,-2,-1,-1,1,1]
res = su.minimumPairRemoval(nums)
ans = 10
assert(res == ans)


# case bug
nums = [2,2,-1,3,-2,2,1,1,1,0,-1]
res = su.minimumPairRemoval(nums)
ans = 9
assert(res == ans)

# case std1
nums = [5,2,3,1]
res = su.minimumPairRemoval(nums)
ans = 2
assert(res == ans)

# case std2
nums = [1,2,2]
res = su.minimumPairRemoval(nums)
ans = 0
assert(res == ans)
