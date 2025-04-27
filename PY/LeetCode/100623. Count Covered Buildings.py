from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings.sort(key=lambda x:(x[0], x[1]))
        # buildings = buildings[1:-1]
        rows = []
        row_cnt = 0

        last = buildings[0][0]
        for building in buildings:
            if last != building[0]:
                if last != -1:
                    rows.append(row_cnt)
                last = building[0]
                row_cnt = 0
            row_cnt += 1
        rows.append(row_cnt)
        # print("rows", rows)

        buildings.sort(key=lambda x:(x[1], x[0]))
        cols = []
        col_cnt = 0

        last = buildings[0][1]
        for building in buildings:
            if last != building[1]:
                if last != -1:
                    cols.append(col_cnt)
                last = building[1]
                col_cnt = 0
            col_cnt += 1
        cols.append(col_cnt)

        # print("cols", cols)

        row_num = sum([max(0, n-2) for n in rows[1:-1]])
        col_num = sum([max(0, n-2) for n in cols[1:-1]])


        ret = min(row_num, col_num)
        # print("ret", ret)
        return ret

    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_dict, col_dict = {}, {}
        for building in buildings:
            if building[0] not in col_dict:
                col_dict[building[0]]  = [building[1], building[1]]
            else:
                col_dict[building[0]] = [min(col_dict[building[0]][0], building[1]), 
                                         max(col_dict[building[0]][1], building[1])]
            
            if building[1] not in row_dict:
                row_dict[building[1]]  = [building[0], building[0]]
            else:
                row_dict[building[1]] = [min(row_dict[building[1]][0], building[0]), 
                                         max(row_dict[building[1]][1], building[0])]

        ret = 0
        for x, y in buildings:
            if col_dict[x][0] < y < col_dict[x][1] and row_dict[y][0] < x < row_dict[y][1]:
                print("xy", x, y)
                ret += 1

        print(col_dict)
        print(row_dict)
        print("ret", ret)
        return ret




su = Solution()
# case std1
n = 5
buildings = [[3,5],[3,2],[5,3],[1,3],[3,3]] # [[1,3],[3,2],[3,3],[3,5],[5,3]]
res = su.countCoveredBuildings(n, buildings)
ans = 1
assert(res == ans)
# case std2
n = 3
buildings = [[1,1],[1,2],[2,1],[2,2]]
res = su.countCoveredBuildings(n, buildings)
ans = 0
assert(res == ans)
# case std4
n = 4
buildings = [[2,4],[1,2],[2,1],[4,3],[3,1],[4,2],[1,4],[2,3],[3,2]]
res = su.countCoveredBuildings(n, buildings)
ans = 0
assert(res == ans)
