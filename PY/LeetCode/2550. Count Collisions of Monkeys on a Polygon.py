import time
class Solution:
    def monkeyMove(self, n: int) -> int:
        # return ((2 ** n) - 2) % (10**9 + 7)
        # return (pow(2, n, 10**9 + 7) - 2) % (10**9 + 7)
        return (pow(2, n) - 2) % (10**9 + 7)
        # return (2*(2 ** (n-1) - 1)) % (10**9 + 7)

        # a = ((2 ** n) - 2) % (10**9 + 7)
        # b = ((2 ** n) % (10**9 + 7) - 2) % (10**9 + 7)
        # c = ((2 ** (n % (10**9 + 7))) % (10**9 + 7) - 2) % (10**9 + 7)
        # d = ((2 ** (n % (33))) % (10**9 + 7) - 2) % (10**9 + 7)
        # print(a, b, c, d)

        # return ((2 ** (n% (10**9 + 7))) % (10**9 + 7) - 2) % (10**9 + 7)
    
        # return ((2 ** n) - 2) % (10**9 + 7)
        # for i in range(100):
        #     # print(((2 ** i) - 2) % (10**9 + 7))
        #     print((2 ** i))

        # tmp = 1
        # for i in range(n):
        #     tmp = tmp << 1
        #     tmp = tmp % (10**9 + 7)
        # return (tmp - 2) % (10**9 + 7)


su = Solution()

tmp = time.time()
print(su.monkeyMove(599161385))
print(time.time() - tmp)

def time_deco(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(func.__name__, t2-t1)
        return res
    return wrapper

# def time_deco(func):
#     t1 = time.time()
#     t2 = time.time()
#     print(t2-t1)
#     return func

@time_deco
def f1(n):
    return 2**n

@time_deco
def f2(n):
    return pow(2, n)

# for i in range(10*10, 10*10+100):
#     f1(i)
#     print(f1(i))
#     print(f2(i))

