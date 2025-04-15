from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers)-1
        while p1 < p2:
            two_sum = numbers[p1] + numbers[p2] 
            if two_sum > target:
                p2 -= 1
            elif two_sum < target:
                p1 += 1
            else:
                ret = [p1+1, p2+1]
                print(ret)
                return ret

su = Solution()

# case std1
numbers = [2,7,11,15]
target = 9
res = su.twoSum(numbers, target)
ans = [1, 2]
assert(res == ans)

# case std2
numbers = [2,3,4]
target = 6
res = su.twoSum(numbers, target)
ans = [1, 3]
assert(res == ans)

# case std3
numbers = [-1,0]
target = -1
res = su.twoSum(numbers, target)
ans = [1, 2]
assert(res == ans)

# case1
numbers = [1,1,2,3]
target = 5
res = su.twoSum(numbers, target)
ans = [3, 4]
assert(res == ans)

# case1
numbers = [1,1,2,3]
target = 2
res = su.twoSum(numbers, target)
ans = [1, 2]
assert(res == ans)

# case1
numbers = [1,1,2,3]
target = 3
res = su.twoSum(numbers, target)
ans = [1, 3]
assert(res == ans)
