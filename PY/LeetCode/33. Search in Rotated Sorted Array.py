from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print("start")
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if left == right:
                return -1
            if right-left == 1:
                if nums[right] == target:
                    return right
                elif nums[left] == target:
                    return left
                else:
                    return -1
            if nums[left] < nums[mid] < nums[right]:
                if target < nums[left] or target > nums[right]:
                    return -1
            if nums[left] <= target < nums[mid]:
                print("case1")
                right = mid - 1
            elif nums[mid] < target <= nums[right]:
                print("case2")
                left = mid + 1
            elif nums[mid] > target and nums[left] >= target:
                if nums[mid] > nums[right]:
                    print("case3")
                    left = mid + 1
                elif nums[mid] < nums[left]:
                    print("case4")
                    right = mid - 1
                else:
                    print("where1")
            elif nums[mid] < target and nums[right] <= target:
                if nums[left] > nums[mid]:
                    print("case5")
                    right = mid - 1
                elif nums[right] < nums[mid]:
                    print("case6")
                    left = mid + 1
                else:
                    print("where2")
            print("lr", left, right)
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid, nums[mid])
            if nums[mid] == target:
                return mid
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
        return -1
            
# 5, 6, 7, 0, 1, 2, 4

# 1, 2, 4, 5, 6, 7, 0
# 2, 4, 5, 6, 7, 0, 1
# 4, 5, 6, 7, 0, 1, 2
# 5, 6, 7, 0, 1, 2, 4
# 6, 7, 0, 1, 2, 4, 5
# 7, 0, 1, 2, 4, 5, 6

# left < mid, right > mid

su = Solution()

# case1 right
nums = [4,5,6,7,0,1,2]
target = 0
ans = 4
res = su.search(nums, target)
assert(res == ans)

# case2 left
nums = [7,0,1,2,4,5,6]
target = 0
ans = 1
res = su.search(nums, target)
assert(res == ans)

# case3 descended
nums = [0,1,2,4,5,6,7]
target = 0
ans = 0
res = su.search(nums, target)
assert(res == ans)

# case4 ascended
# nums = [7,6,5,4,3,2,0]
nums = [7,4,5,6]
target = 6
ans = 3
res = su.search(nums, target)
assert(res == ans)

# case5 1
nums = [1]
target = 0
ans = -1
res = su.search(nums, target)
assert(res == ans)

# case1 mid left
nums = [5, 6, 7, 0, 1, 2, 4]
target = 6
ans = 1
res = su.search(nums, target)
assert(res == ans)

# case6 2
nums = [4,5]
target = 0
ans = -1
res = su.search(nums, target)
assert(res == ans)

# case7 3
nums = [5, 3]
target = 3
ans = 1
res = su.search(nums, target)
assert(res == ans)


# case8
nums = [4,5,6]
target = 6
ans = 2
res = su.search(nums, target)
assert(res == ans)

# case9
nums = [4,5,6,7,0,1,2]
target = 3
ans = -1
res = su.search(nums, target)
assert(res == ans)

# case10
nums = [1]
target = 0
ans = -1
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
ans = 6
res = su.search(nums, target)
assert(res == ans)

# case n12
nums = [2, 4, 5, 6, 7, 0, 1]
target = 0
ans = 5
res = su.search(nums, target)
assert(res == ans)

# case n13
nums = [2, 4, 5, 6, 7, 0, 1]
target = 7
ans = 4
res = su.search(nums, target)
assert(res == ans)

# case n14
nums = [2, 4, 5, 6, 7, 0, 1]
target = 4
ans = 1
res = su.search(nums, target)
assert(res == ans)

# 7, 0, 1, 2, 4, 5, 6

# case n21
nums = [7, 0, 1, 2, 4, 5, 6]
target = 7
ans = 0
res = su.search(nums, target)
assert(res == ans)

# case n22
nums = [7, 0, 1, 2, 4, 5, 6]
target = 0
ans = 1
res = su.search(nums, target)
assert(res == ans)

# case n23
nums = [7, 0, 1, 2, 4, 5, 6]
target = 1
ans = 2
res = su.search(nums, target)
assert(res == ans)

# case n24
nums = [7, 0, 1, 2, 4, 5, 6]
target = 6
ans = 6
res = su.search(nums, target)
assert(res == ans)


