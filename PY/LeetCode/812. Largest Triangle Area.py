from typing import List
import math

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    trans = lambda a, b: (a[0]-b[0], a[1]-b[1])
                    edge1 = math.hypot(*trans(points[i], points[j]))
                    edge2 = math.hypot(*trans(points[i], points[k]))
                    edge3 = math.hypot(*trans(points[j], points[k]))
                    p = (edge1 + edge2 + edge3) / 2
                    tmp = p*(p-edge1)*(p-edge2)*(p-edge3)
                    if tmp > 0:
                        res = max(res, math.sqrt(tmp))
        print(res)
        return res

points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
su = Solution()
su.largestTriangleArea(points)

points = [[35,-23],[-12,-48],[-34,-40],[21,-25],[-35,-44],[24,1],[16,-9],[41,4],[-36,-49],[42,-49],[-37,-20],[-35,11],[-2,-36],[18,21],[18,8],[-24,14],[-23,-11],[-8,44],[-19,-3],[0,-10],[-21,-4],[23,18],[20,11],[-42,24],[6,-19]]
su = Solution()
su.largestTriangleArea(points)
