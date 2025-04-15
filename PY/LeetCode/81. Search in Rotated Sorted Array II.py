from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print("**************************************************************")
        left, right = 0, len(nums) - 1
        while left <= right:
            print(left, right)
            mid = (left+right)//2
            if nums[mid] == target:
                return True


            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        print("**************************************************************")             
        return False

su = Solution()

# case1 right
nums = [4,5,6,7,0,1,2]
target = 0
ans = True
res = su.search(nums, target)
assert(res == ans)

# case2 left
nums = [7,0,1,2,4,5,6]
target = 0
ans = True
res = su.search(nums, target)
assert(res == ans)

# case3 descended
nums = [0,1,2,4,5,6,7]
target = 0
ans = True
res = su.search(nums, target)
assert(res == ans)

# case4 ascended
# nums = [7,6,5,4,3,2,0]
nums = [7,4,5,6]
target = 6
ans = True
res = su.search(nums, target)
assert(res == ans)

# case5 1
nums = [1]
target = 0
ans = False
res = su.search(nums, target)
assert(res == ans)

# case1 mid left
nums = [5, 6, 7, 0, 1, 2, 4]
target = 6
ans = True
res = su.search(nums, target)
assert(res == ans)

# case6 2
nums = [4,5]
target = 0
ans = False
res = su.search(nums, target)
assert(res == ans)

# case7 3
nums = [5, 3]
target = 3
ans = True
res = su.search(nums, target)
assert(res == ans)


# case8
nums = [4,5,6]
target = 6
ans = True
res = su.search(nums, target)
assert(res == ans)

# case9
nums = [4,5,6,7,0,1,2]
target = 3
ans = False
res = su.search(nums, target)
assert(res == ans)

# case10
nums = [1]
target = 0
ans = False
res = su.search(nums, target)
assert(res == ans)

# 2, 4, 5, 6, 7, 0, 1
# 4, 5, 6, 7, 0, 1, 2
# 5, 6, 7, 0, 1, 2, 4
# 6, 7, 0, 1, 2, 4, 5
# 7, 0, 1, 2, 4, 5, 6

# case n11
nums = [2, 4, 5, 6, 7, 0, 1]
target = 1
ans = True
res = su.search(nums, target)
assert(res == ans)

# case n12
nums = [2, 4, 5, 6, 7, 0, 1]
target = 0
ans = True
res = su.search(nums, target)
assert(res == ans)

# case n13
nums = [2, 4, 5, 6, 7, 0, 1]
target = 7
ans = True
res = su.search(nums, target)
assert(res == ans)

# case n14
nums = [2, 4, 5, 6, 7, 0, 1]
target = 4
ans = True
res = su.search(nums, target)
assert(res == ans)

# 7, 0, 1, 2, 4, 5, 6

# case n21
nums = [7, 0, 1, 2, 4, 5, 6]
target = 7
ans = True
res = su.search(nums, target)
assert(res == ans)

# case n22
nums = [7, 0, 1, 2, 4, 5, 6]
target = 0
ans = True
res = su.search(nums, target)
assert(res == ans)

# case n23
nums = [7, 0, 1, 2, 4, 5, 6]
target = 1
ans = True
res = su.search(nums, target)
assert(res == ans)

# case n24
nums = [7, 0, 1, 2, 4, 5, 6]
target = 6
ans = True
res = su.search(nums, target)
assert(res == ans)


# 81 case
# 7, 0, 1, 2, 4, 5, 6

# case n21
nums = [7, 0, 1, 1, 1, 2, 2, 2, 4, 5, 6]
target = 7
ans = True
res = su.search(nums, target)
assert(res == ans)

# case n22
nums = [7, 8, 9, 9, 10, 0, 1, 2, 4, 5, 6]
target = 0
ans = True
res = su.search(nums, target)
# print(res)
assert(res == ans)

# case n23 bug
nums = [1,0,1,1,1]
target = 0
ans = True
res = su.search(nums, target)
assert(res == ans)

# case n24 bug2
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2
ans = True
res = su.search(nums, target)
assert(res == ans)


# case n25
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 2
ans = False
res = su.search(nums, target)
assert(res == ans)


# case n256
nums = [4,5,1,2,3,3,3,3]
target = 3
ans = True
res = su.search(nums, target)
assert(res == ans)

# case n257
nums = [2,4,5,1,1,1,2,2,2]
target = 4
ans = True
res = su.search(nums, target)
assert(res == ans)