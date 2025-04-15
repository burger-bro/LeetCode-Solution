class Solution:
    def isPowerOfThree0(self, n: int) -> bool:
        if n <= 0: return False
        res = 0
        res_set = set()
        cnt = 0
        while res <= 2**31 -1:
            res = 3**cnt
            res_set.add(res)
            cnt += 1
        print(res_set)
        return n in res_set
    
    def isPowerOfThree1(self, n: int) -> bool:
        if n <= 0: return False
        res = n
        while res != 1:
            res, rem = divmod(res, 3)
            if rem != 0:
                return False
        return True

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

Solution().isPowerOfThree(2)
