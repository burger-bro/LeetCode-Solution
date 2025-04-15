from typing import List
from collections import OrderedDict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        num_dict = OrderedDict()
        for n in nums:
            num_dict[n] = num_dict.get(n, 0) + 1
        ret = []
        flag = True
        while flag:
            tmp = []
            flag = False
            for k, v in num_dict.items():
                if v == 0: 
                    continue
                flag = True
                tmp.append(k)
                num_dict[k] = v - 1
            if tmp:
                ret.append(tmp)
        print(ret)
        return ret
    
su = Solution()

# nums = [1,3,4,1,2,3,1]
# ans = [[1,3,4,2],[1,3],[1]]
# res = su.findMatrix(nums)
# assert(ans == res)

nums = [1,2,3,4]
ans = [[1,2,3,4]]
res = su.findMatrix(nums)
assert(ans == res)

nums = [1,2,3,3,4]
ans = [[1,2,3,4],[3]]
res = su.findMatrix(nums)
assert(ans == res)

nums = [1]
ans = [[1]]
res = su.findMatrix(nums)
assert(ans == res)

nums = [1,1,1,1,1]
ans = [[1],[1],[1],[1],[1]]
res = su.findMatrix(nums)
assert(ans == res)

nums = [1,2,99,99,99]
ans = [[1,2,99],[99],[99]]
res = su.findMatrix(nums)
assert(ans == res)


t_dict = OrderedDict({"1":1, "2":2, "3":3, "9":9, "10":10, "100":100})

t_dict = {"1":1, "2":2, "3":3, "9":9, "10":10, "100":100}

print(t_dict)

for k, v in t_dict.items():
    if k == "3":
        del t_dict["3"]
    print(t_dict)

