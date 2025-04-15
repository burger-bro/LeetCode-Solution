from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)

        ans = []
        n = len(nums)
        for i in range(n):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            # if nums[i] > target:
            #     break
            if n - i < 4:
                break
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                # if nums[i] + nums[j] > target:
                #     break
                if n - j < 3:
                    break
                left = j + 1
                right = n - 1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if left > j + 1 and nums[left] == nums[left-1]:
                        left += 1
                        continue
                    if right < n - 1 and nums[right] == nums[right+1]:
                        right -= 1
                        continue
                    if tmp == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                    if tmp > target:
                        right -= 1
                    elif tmp < target:
                        left += 1
        print(ans)
        return ans





su = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
res1 = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# assert(su.fourSum(nums, target) == res1)

nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
res2 = [[-5,-4,-3,1]]
# assert(su.fourSum(nums, target) == res2)

nums = [-3,-2,-1,0,0,1,2,3]
target = 0
res3 = [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
assert(su.fourSum(nums, target) == res3)
