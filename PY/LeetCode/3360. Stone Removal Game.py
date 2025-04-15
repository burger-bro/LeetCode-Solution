class Solution(object):
    def canAliceWin(self, n):
        """
        爱丽丝先手移除10记为x，随后两边交替移除x=x-1，直到x<remain
        """
        x = 10
        is_alice = True
        while n >= x:
            n -= x
            x -= 1
            is_alice = not is_alice
        return not is_alice
        

    def canAliceWin(self, n):
        """
        S = (7 8 9 10)    (7 + 10)*n/2    (10 + x)*(10-x+1)//2
        """
        x = 10
        is_alice = True
        while n >= x:
            n -= x
            x -= 1
            is_alice = not is_alice
        return not is_alice

su = Solution()

n = 20
res = su.canAliceWin(n)
ans = False
assert(res == ans)

n = 12
res = su.canAliceWin(n)
ans = True
assert(res == ans)

n = 1
res = su.canAliceWin(n)
ans = False
assert(res == ans)

