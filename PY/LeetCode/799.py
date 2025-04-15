from collections import deque
import heapq
from queue import PriorityQueue

# heap = [4,2,1,6,3]
# a = heapq.heapify(heap)
# print(heap[0])
# print(heapq.heappop(heap))

# exit(0)
class Solution:


    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        
        """
        print("*******************begin*******************")

        glass_dict = {}

        maximum = sum([i for i in range(1,101)])
        if poured >= maximum: return 1

        queue = [[1, 1, 1, (0,0)]] # time   diff   speed
        heapq.heapify(queue)

        remind = poured
        while remind > 0:
            print(queue)
            soon_fill_up = queue[0]  #取最快填满的
            fill_time = soon_fill_up[0]
            print("fill_time", fill_time, remind)
            # print("sum:", sum(q[2] for q in queue))
            all_fill_num = fill_time
            if all_fill_num <= remind:
                print("if")
                remind -= all_fill_num
                for q in queue:
                    q[1] -= fill_time*q[2]
                    q[0] -= fill_time
                while queue and (queue[0][1]==0 or queue[0][0]==0):
                    pop = heapq.heappop(queue)
                    print("pop:", pop)
                    if pop[3][0] == query_row and pop[3][1] == query_glass:
                        return 1

                    # heapq.heappush(queue, [2/pop[2], 1, pop[2]/2, (pop[3][0]+1, pop[3][1])])
                    # heapq.heappush(queue, [2/pop[2], 1, pop[2]/2, (pop[3][0]+1, pop[3][1]+1)])

                    if (pop[3][0]+1, pop[3][1]) in glass_dict:
                        glass_dict[(pop[3][0]+1, pop[3][1])][2] += pop[2]/2
                        glass_dict[(pop[3][0]+1, pop[3][1])][0] = glass_dict[(pop[3][0]+1, pop[3][1])][1]/glass_dict[(pop[3][0]+1, pop[3][1])][2]
                    else:
                        new = [2/pop[2], 1, pop[2]/2, (pop[3][0]+1, pop[3][1])]
                        glass_dict[(pop[3][0]+1, pop[3][1])] = new
                        heapq.heappush(queue, new)

                    if (pop[3][0]+1, pop[3][1]+1) in glass_dict:
                        glass_dict[(pop[3][0]+1, pop[3][1]+1)][2] += pop[2]/2
                        glass_dict[(pop[3][0]+1, pop[3][1]+1)][0] = glass_dict[(pop[3][0]+1, pop[3][1])][1]/glass_dict[(pop[3][0]+1, pop[3][1]+1)][2]
                    else:
                        new = [2/pop[2], 1, pop[2]/2, (pop[3][0]+1, pop[3][1]+1)]
                        glass_dict[(pop[3][0]+1, pop[3][1]+1)] = new
                        heapq.heappush(queue, new)
                    heapq.heapify(queue)
                    # heapq.heappush(queue, [2/pop[2], 1, pop[2]/2, (pop[3][0]+1, pop[3][1]+1)])
            else:
                print("else")
                actual_fill_num = remind
                for q in queue:
                    print("1", q)
                    q[1] = q[1] - actual_fill_num*q[2]
                    print("2", q)
                    if q[3][0] == query_row and q[3][1] == query_glass:
                        return 1-q[1]
                remind = 0

        return 0


    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [[0]*(i+1) for i in range(query_row+1)]
        row[0][0] = poured
        for i in range(query_row):
            for j in range(i+1):
                # print(row[i][j])
                if row[i][j]-1 < 0: continue
                exceed = (row[i][j]-1)/2
                # print(exceed)
                row[i+1][j] += exceed
                row[i+1][j+1] += exceed
        for r in row:
            print(r)
        return min(row[query_row][query_glass], 1)


su = Solution()

# case bug
# poured = 25
# query_row = 6
# query_glass = 1
# res = su.champagneTower(poured, query_row, query_glass)
# ans = 0.25
# print(res)
# exit(0)
# assert(res == ans)
# exit(0)

# case bug
poured = 9
query_row = 3
query_glass = 3
res = su.champagneTower(poured, query_row, query_glass)
ans = 0.25
print(res)
assert(res == ans)
# exit(0)

# case bug
poured = 9
query_row = 3
query_glass = 2
res = su.champagneTower(poured, query_row, query_glass)
ans = 1.00000
assert(res == ans)


# case std1
poured = 1
query_row = 1
query_glass = 1
res = su.champagneTower(poured, query_row, query_glass)
ans = 0.00000
assert(res == ans)

# case std2
poured = 2
query_row = 1
query_glass = 1
res = su.champagneTower(poured, query_row, query_glass)
ans = 0.50000
print(res)
assert(res == ans)

# case std2
poured = 6
query_row = 2
query_glass = 0
res = su.champagneTower(poured, query_row, query_glass)
ans = 0.75000
print(res)
assert(res == ans)

# # case std3
poured = 100000009
query_row = 33
query_glass = 17
res = su.champagneTower(poured, query_row, query_glass)
ans = 1.00000
print(res)
assert(res == ans)
