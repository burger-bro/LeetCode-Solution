# import pytest

# def sum(a, b):
#     return a + b

# class TestDemo:
#     def test_case1(self):
#         assert not sum(1, 4) == 3
    
#     def test_case2(self):
#         assert sum(1, 4) == 5

# if __name__ == '__main__':
#     pytest.main()

# n = 10
# def A(i):
#     # (1+2*(i)) % (n|1)
#     tmp1 = 1 + 2 * i
#     tmp2 = (n | 1)
#     # print(tmp1, tmp2)
#     return tmp1 % tmp2

# print(A(0))
# print(A(1))
# print(A(2))
# print(A(3))
# print(A(4))
# print(A(5))
# print(A(6))
# print(A(7))
# print(A(8))
# print(A(9))
# print(A(10))
# print(A(11))
# print(A(12))
# print(A(13))
# print(A(14))

from sortedcontainers import SortedList

ssl = SortedList([555])
print(ssl)
ssl.add(333)
print(ssl)
ssl.add(444)
print(ssl)
ssl.add(999)
print(ssl)
ssl.add(5000)
print(ssl)
ssl.add(0)
print(ssl)

print(ssl.bisect_left(0))
print(ssl.bisect_left(-100))
print(ssl.bisect_left(999))
print(ssl.bisect_left(555))


exit(0)

def a():
    print("start")
    x = 0
    def b(y):
        nonlocal x
        x += y
        return x
    print("end")
    return b

c = a()
print(c(3))
print(c(3))
print(c(3))
d = a()
print(d(3))
print(d(3))
print(c(3))
print("cd", c.__class__, c.__init__, c.__)
print(c(3))

exit(0)
class TestA:
    num = 0
    def test1(self):
        assert self.num == 0

A = TestA()
A.test1()

a = [0, -2, 4, 56, -24, 64, -62, 14, 67, 43, -97, -34]

from collections import Counter
a = [1,3,5,7,9]
print(Counter(a))

