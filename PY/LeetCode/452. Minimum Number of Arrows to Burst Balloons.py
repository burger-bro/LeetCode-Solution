from typing import List

class Solution:
    def findMinArrowShots0(self, points: List[List[int]]) -> int:
        ans = 0
        old_points = points
        while old_points:
            ans += 1
            num_dict = {}
            for point in old_points:
                for i in range(point[0], point[1]+1):
                    num_dict[i] = num_dict.get(i, 0) + 1
            # print(num_dict)
            max_key = None
            max_val = -float("inf")
            for k, v in num_dict.items():
                if v > max_val:
                    max_key = k
                    max_val = v
            # print(max_key)
            new_points = []
            for point in old_points:
                if not point[0] <= max_key <= point[1]:
                    new_points.append(point)
            # print(new_points)
            old_points = new_points
        return ans

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        intersections = []
        points.sort(key=lambda x:x[0])
        # print(points)
        for point in points:
            if not intersections:
                intersections.append(point)
                continue
            for i in range(len(intersections)):
                if point[0] <= intersections[i][1]:
                    intersections[i][0] = max(intersections[i][0], point[0])
                    intersections[i][1] = min(intersections[i][1], point[1])
                    break
            else:
                intersections.append(point)
        # print(intersections)
        return len(intersections)
                    
                


su = Solution()

points = [[10,16],[2,8],[1,6],[7,12]]
ans = 2
res = su.findMinArrowShots(points)
assert(res == ans)

points = [[1,2],[3,4],[5,6],[7,8]]
ans = 4
res = su.findMinArrowShots(points)
assert(res == ans)

points = [[1,2],[2,3],[3,4],[4,5]]
ans = 2
res = su.findMinArrowShots(points)
assert(res == ans)

points = [[1,1], [2,2]]
ans = 2
res = su.findMinArrowShots(points)
assert(res == ans)

points = [[1,1], [1,1], [1,2], [1,2]]
ans = 1
res = su.findMinArrowShots(points)
assert(res == ans)

# xxxxxxxxx
#     xx
#     xxxxx
#        xxxxxxxxx
#            xxxxx
#               xxxxx