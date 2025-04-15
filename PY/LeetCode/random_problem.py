from itertools import combinations

class X:
    pass

a = X()
b = X()
c = X()
d = X()

def helper(x):
    if x is a:
        return 'a'
    elif x is b:
        return 'b'
    elif x is c:
        return 'c'
    elif x is d:
        return 'd'

X.__repr__ = helper

test_list = [a, b, c, d]
test_set = {a, b, c, d}
# test_set = {1, 3, 6, 4}

for s in test_set:
    print(s, hash(s))

it = combinations(test_set, r=2)
for x in it:
    print(x)

print("24256")
