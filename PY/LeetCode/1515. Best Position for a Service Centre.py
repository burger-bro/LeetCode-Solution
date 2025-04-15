from typing import List
from math import sqrt
from decimal import Decimal, getcontext

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # 使用数学方法，构造L = Sigma(sqrt((x-xi)+(y-yi)))，梯度下降
        if len(positions) == 1: return 0
        def L(x, y):
            ss = 0
            for xi, yi in positions:
                ss += sqrt((x - xi)**2 + (y-yi)**2)  # 欧式距离->曼哈顿距离？ sqrt的必要性？
            return ss
        
        def get_gradient(x, y):
            px = (L(x+step, y) - L(x, y)) / step
            py = (L(x, y+step) - L(x, y)) / step
            # 归一化
            return px, py

        x, y = 0, 0
        step = 2
        epoch = 10000
        cnt = 0
        remind = 10
        while True:
            cnt += 1
            # print(step, remind)
            if cnt % remind == 0:
                remind *= 10 if remind < 1000 else 1
                step *= 0.2
            nx, ny = get_gradient(x, y)
            x -= nx*step
            y -= ny*step
            if cnt > epoch:
                return L(x, y)
            # print(x,y,L(x,y))

    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # 使用数学方法，构造L = Sigma(sqrt((x-xi)+(y-yi)))，梯度下降
        if len(positions) == 1: return 0
        def L(x, y):
            ss = 0
            for xi, yi in positions:
                ss += sqrt((x - xi)**2 + (y-yi)**2)  # 欧式距离->曼哈顿距离？ sqrt的必要性？
            return ss
        
        def get_gradient(x, y):
            px = (L(x+step, y) - L(x, y)) / step
            py = (L(x, y+step) - L(x, y)) / step
            # 归一化
            length = sqrt(px**2 + py**2)
            if length == 0:
                return 0, 0  # 避免除以零的情况
            x_normalized = px / length
            y_normalized = py / length
            px, py = x_normalized, y_normalized
            return px, py

        x, y = 0, 0
        step = 40
        epoch = 20000
        cnt = 0
        remind = 10
        while True:
            cnt += 1
            # print(step, remind)

            if step > 10**(-5) and cnt % remind == 0:
                remind *= 10 if remind < 1000 else 1
                step *= 0.1

            # if cnt % 1000 == 0:
            #     step *= 0.01

            nx, ny = get_gradient(x, y)

            nx_n = nx*step
            nx_y = ny*step

            x -= nx_n
            y -= nx_y
            if cnt > epoch:
                return L(x, y)
            print(x,y,L(x,y),nx,ny,step)


from typing import List
from math import sqrt
import numpy as np

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # 使用数学方法，构造L = Sigma(sqrt((x-xi)+(y-yi)))，梯度下降
        if len(positions) == 1: return 0
        def L(x, y):
            ss = 0
            for xi, yi in positions:
                ss += sqrt((x - xi)**2 + (y-yi)**2)  # 欧式距离->曼哈顿距离？ sqrt的必要性？
            return ss
        
        def get_gradient(x, y):
            px = (L(x+step, y) - L(x, y)) / step
            py = (L(x, y+step) - L(x, y)) / step
            # 归一化
            length = sqrt(px**2 + py**2)
            if length == 0:
                return 0, 0  # 避免除以零的情况
            x_normalized = px / length
            y_normalized = py / length
            px, py = x_normalized, y_normalized
            return px, py
        v = np.sum(np.array(x) for x in positions)/len(positions)
        x, y = v
        # x, y = 0, 0
        step = 2
        epoch = 1000
        cnt = 0
        pg = np.zeros(2)
        while True:
            cnt += 1
            # print(step, remind)
            nx, ny = get_gradient(x, y)

            g = np.zeros(2) + (nx, ny)

            if np.dot(g,pg) < 0:
                step /= 2

            x -= nx*step
            y -= ny*step
            if cnt > epoch:
                return L(x, y)
            pg = g
            print(x, y, L(x,y))

# import numpy as np

# class Solution:
#     def getMinDistSum(self, positions: List[List[int]]) -> float:

        # def grad(v):
        #     g = np.zeros(2)
        #     for x,y in positions:
        #         vt = v - (x,y)
        #         norm = np.linalg.norm(vt)
        #         if norm != 0:
        #             g += vt/norm
        #     return g

#         v = np.sum(np.array(x) for x in positions)/len(positions)
#         lr = 1
#         pg = np.zeros(2)
#         for i in range(1000):
#             g = grad(v)
#             v -= lr*g

#             if np.dot(g,pg) < 0:
#                 lr /= 2

#             pg = g

#             if lr*np.linalg.norm(g) < 1e-7:
#                 break



#         return sum( np.linalg.norm(v-(x,y)) for x,y in positions)

su = Solution()

# case bug4
positions = [[27,90],[99,75],[99,38]]
res = su.getMinDistSum(positions)
ans = 109.30317
print(res, abs(res-ans))
assert(abs(res-ans) < 0.00001)

# case bug3
positions = [[58,32],[41,21]]
res = su.getMinDistSum(positions)
ans = 20.24846
print(res, abs(res-ans))
assert(abs(res-ans) < 0.00001)

# case bug2
positions = [[0,1],[1,0],[1,2],[2,1],[1,1]]
res = su.getMinDistSum(positions)
ans = 4.00000
print(res, abs(res-ans))
assert(abs(res-ans) < 0.00001)

# case bug
positions = [[1,1]]
res = su.getMinDistSum(positions)
ans = 0.00000
print(res, abs(res-ans))
assert(abs(res-ans) < 0.00001)

# case std1
positions = [[0,1],[1,0],[1,2],[2,1]]
res = su.getMinDistSum(positions)
ans = 4.00000
print(res, abs(res-ans))
assert(abs(res-ans) < 0.00001)

# case std2
positions = [[1,1],[3,3]]
res = su.getMinDistSum(positions)
ans = 2.82843
assert(abs(res-ans) < 0.00001)

# case perf
positions = [[0, 1], [1, 0], [1, 2], [2, 1], [3, 2], [0, 1], [1, 0], [1, 2], [2, 1], [3, 2], [0, 1], [1, 0], [1, 2], [2, 1], [3, 2], [0, 1], [1, 0], [1, 2], [2, 1], [3, 2], [0, 1], [1, 0], [1, 2], [2, 1], [3, 2], [0, 1], [1, 0], [1, 2], [2, 1], [3, 2], [0, 1], [1, 0], [1, 2], [2, 1], [3, 2], [0, 1], [1, 0], [1, 2], [2, 1], [3, 2], [0, 1], [1, 0], [1, 2], [2, 1], [3, 2], [0, 1], [1, 0], [1, 2], [2, 1], [3, 2]]
res = su.getMinDistSum(positions)
ans = 59.91516
assert(abs(res-ans) < 0.00001)
