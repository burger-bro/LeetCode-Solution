from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,4,8,16,32]
        # k = 4

        remind = []
        for n in nums:
            remind.append(n%k)
        print(remind)

        # self.helper(nums, k, 0)
        # self.helper(nums, k, 1)
        # self.helper(nums, k, 2)


        # self.helper(nums[::-1], k, 0)
        # self.helper(nums[::-1], k, 1)
        # self.helper(nums[::-1], k, 2)
        pass

    # def resultArray(self, nums: List[int], k: int) -> List[int]:
    #     ret = []
    #     for x in range(k):
    #         cnt = 0
    #         for i in range(len(nums)):
    #             product = nums[i]
    #             for j in range(i+1, len(nums)):
    #                 if product % k == x:
    #                     cnt += 1
    #                 product *= nums[j]
    #             if product % k == x: cnt += 1
    #         ret.append(cnt)
        #     print("ret", ret)
        # return ret

    def resultArray(self, nums: List[int], k: int) -> List[int]:
        nums = [10, 2]
        k = 4

        remind = []
        for n in nums:
            remind.append(n%k)

        ret = []
        for x in range(k):
            cnt = 0
            for i in range(len(remind)):
                product = remind[i]
                for j in range(i+1, len(remind)):
                    if product % k == x:
                        cnt += 1
                    # elif product > x:
                    #     break
                    product *= remind[j]
                if product % k == x: cnt += 1
            ret.append(cnt)
        print("ret", ret)
        return ret

    def resultArray(self, nums: List[int], k: int) -> List[int]:
        remind = []
        for n in nums:
            remind.append(n%k)


        n = len(nums)
        result = [0] * k
        for l in range(n):
            product = 1
            for r in range(l, n):
                product = (product * remind[r]) % k
                # The corresponding i is l - 1, j is r + 1
                # The remaining subarray is nums[l..r]
                # The operation is to remove nums[0..i] (prefix) and nums[j..n-1] (suffix)
                # So the count is 1 for this subarray
                result[product] += 1
        return result

    def resultArray(self, nums: List[int], k: int) -> List[int]:
        print("**************** start ****************")
        n = len(nums)
        result = [0] * k
        current = [0] * k
        for num in nums:
            mod = num % k
            next_dp = [0] * k
            next_dp[mod] += 1
            for x in range(k):
                if current[x]:
                    new_x = (x * mod) % k
                    next_dp[new_x] += current[x]
            for x in range(k):
                result[x] += next_dp[x]
            current = next_dp
            print(current)
        print("res", result)
        return result

    # def helper(self, nums, k, x):
    #     cnt = 0
    #     for i in range(len(nums)):
    #         product = nums[i]
    #         for j in range(i+1, len(nums)):
    #             # print(i, j, product)
    #             if product % k == x:
    #                 cnt += 1
    #             else:
    #                 break
    #             product *= nums[j]
    #     print("help cnt:", cnt)
    #     return cnt

su = Solution()
# case std1
nums = [1,2,3,4,5]
"""
4 = 3*1 ~ 1
5 = 3*1 ~ 2
4*5 = 3*8 ~ 2
4*5 = 20 = 3*6 ~ 2
4*5 = (3*1+1)*(3*1+2) = 3*3*(1*1) + 3*1*(2) + 3*1*(1) + 2*1
"""
k = 3
res = su.resultArray(nums, k)
ans = [9,2,4]
assert(res == ans)

# case std2
nums = [1,2,4,8,16,32]
k = 4
res = su.resultArray(nums, k)
ans = [18,1,2,0]
assert(res == ans)
        