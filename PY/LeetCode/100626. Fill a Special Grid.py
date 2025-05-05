from typing import List

class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        grid = [[-1]*N for _ in range(N)]
        def makeGrid(xy0, xy1, min_, max_):
            if xy0 == xy1:
                grid[xy0[0]][xy0[1]] = min_
            middle = [(xy0[0]+xy1[0])//2, (xy0[1]+xy1[1])//2]
            _range = (max_-min_)//4
            # top-right
            n_max_ = (xy1[0]-middle[0]+1)*(middle[1]-xy0[1]+1)
            makeGrid((middle[0]+1, xy0[1]), (xy1[0], middle[1]), min_, min_+n_max_)
            # bottom-right
            n_max2 = (xy1[0]-middle[0])*(middle[1]-xy0[1])
            makeGrid((middle[0]+1, middle[1]+1), xy1, min_+n_max_+1, min_+n_max_+n_max2)
            # bottom-left
            n_max3 = (middle[0]-xy0[0]+1)*(xy1[1]-middle[1])
            makeGrid((xy0[0], middle[1]+1), (middle[0], xy1[1]), min_+n_max_+n_max2+1, min_+n_max_+n_max2+n_max3)
            # top-left
            makeGrid(xy0, middle, min_+n_max_+n_max2+n_max3+1, max_)


        makeGrid((0, 0), (2**N, 2**N), 0, 2**(2*N)-1)
        print(grid)
        return grid

    def specialGrid(self, N):
        length = 2**N
        grid = [[0 for _ in range(length)] for _ in range(length)]
        def makeGrid(x, y, n, cur_val):
            if n == 1:
                grid[x][y] = cur_val
                return
            middle = n // 2
            range_ = middle * middle
            makeGrid(x, y + middle, middle, cur_val)
            makeGrid(x + middle, y + middle, middle, cur_val+range_)
            makeGrid(x + middle, y, middle, cur_val+2*range_)
            makeGrid(x, y, middle, cur_val+3*range_)
            return 
        
        makeGrid(0, 0, length, 0)
        return grid

su = Solution()
# case std1
N = 0
res = su.specialGrid(N)
ans = [[0]]
assert(res == ans)

# case std2
N = 1
res = su.specialGrid(N)
ans = [[3,0],[2,1]]
assert(res == ans)

# case std2
N = 2
res = su.specialGrid(N)
ans =  [[15,12,3,0],[14,13,2,1],[11,8,7,4],[10,9,6,5]]
assert(res == ans)

