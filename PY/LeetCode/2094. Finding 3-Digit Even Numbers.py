from typing import List
from collections import Counter, defaultdict

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        ret = set()
        m = len(digits)
        for i in range(m):
            if digits[i] == 0: continue
            for j in range(m):
                if j == i: continue
                for k in range(m):
                    if k == j or k == i: continue
                    if digits[k] % 2 == 0:
                        tmp = digits[i]*100+digits[j]*10+digits[k] 
                        ret.add(tmp)
        return sorted(list(ret))

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ret = []
        d = Counter(digits)
        for candi in range(100, 1000, 2):
            c_d = defaultdict(int)
            tmp = candi
            while tmp:
                c_d[tmp%10] += 1
                tmp //= 10
            for k, v in c_d.items():
                if d[k] < v:
                    break
            else:
                ret.append(candi)

        return ret

su = Solution()
# case std1
digits = [2,1,3,0]

d1 = Counter("11222")
d2 = Counter("12")
print(d1)
print(d2)
print(d1&d2)
