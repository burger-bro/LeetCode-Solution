from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ret = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i+1, len(prices)):
                if prices[j] < prices[i]:
                    discount = prices[j]
                    break
            ret.append(prices[i]-discount)
        print(ret)
        return ret

su = Solution()
# case std1
prices = [8,4,6,2,3]
res = su.finalPrices(prices)
ans = [4,2,4,2,3]
assert(res == ans)




