from typing import List
from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        理想情况下 如果有x颜色的兔子n只 则他能够看到n-1只兔子
        1所以当一只兔子看见了n-1只和他一样的兔子 
        则可以假定至少存在n只该颜色兔子
        而后续若也存在n-1只 可以优先归类到一起
        """

        a_cnt = Counter(answers)
        ret = 0
        for k,v in a_cnt.items():
            maybe_colour = ceil(v / (k+1))
            ret += maybe_colour*(k+1)

        print(ret)
        return ret
        

su = Solution()
# case std1
answers = [1,1,2]
# x:2 y:3
# [1,1,1,2]
# [1,1,2,2]

# [1,1,1]
res = su.numRabbits(answers)
ans = 5
assert(res == ans)

# case std2
answers = [10,10,10]
res = su.numRabbits(answers)
ans = 11
assert(res == ans)
