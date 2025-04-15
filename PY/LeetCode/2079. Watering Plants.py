from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur = capacity
        steps = 0
        i = 0
        while i < len(plants):
            # print(steps)
            if cur >= plants[i]:
                steps += 1
                cur -= plants[i]
                i += 1
            else:
                steps += 2*i
                cur = capacity
        print("res:", steps)
        return steps



su = Solution()
# case std1
plants = [2,2,3,3]
capacity = 5
res = su.wateringPlants(plants, capacity)
ans = 14
assert(res == ans)

# case std2
plants = [1,1,1,4,2,3]
capacity = 4
res = su.wateringPlants(plants, capacity)
ans = 30
assert(res == ans)

# case std3
plants = [7,7,7,7,7,7,7]
capacity = 8
res = su.wateringPlants(plants, capacity)
ans = 49
assert(res == ans)

# case1 min 
plants = [1]
capacity = 9
res = su.wateringPlants(plants, capacity)
ans = 1
assert(res == ans)

# case2 max
plants = [2,5,36,64,3,124,235]
capacity = 999999
res = su.wateringPlants(plants, capacity)
ans = len(plants)
assert(res == ans)

# case2 max
plants = [5, 5]
capacity = 4
res = su.wateringPlants(plants, capacity)
ans = len(plants)
print(res)
# assert(res == ans)

