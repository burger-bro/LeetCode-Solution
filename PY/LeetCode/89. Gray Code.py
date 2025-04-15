from typing import List
from collections import deque
        # 00
        # 01
        # 11
        # 10

        # 0000
        # 0001
        # 0011
        # 0010
        # 0110
        # 0111
        # 0101
        # 0100

        # 1100
        # 1101
        # 1111
        # 1110
        # 1010
        # 1011
        # 1001
        # 1000
        # 

class Solution:
    def grayCode(self, n: int) -> List[int]:
        queue = deque(['0', '1'])
        for i in range(1, n):
            length = len(queue)
            for s in range(length):
                queue.append('0'+queue.popleft())
            for s in range(length-1, -1, -1):
                queue.append('1'+queue[s][1:])
        # print(queue)
        for i in range(len(queue)):
            queue[i] = int(queue[i], 2)
        return list(queue)

su = Solution()
n = 2
res = su.grayCode(n)
ans = [0,1,3,2]
print(res)
assert(res == ans)

# n = 1
# res = su.grayCode(n)
# ans = [0,1]
# assert(res == ans)

# n = 16
# res = su.grayCode(n)
# print(res)
