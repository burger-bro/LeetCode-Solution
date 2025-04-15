
def f1():
    a = [1,3,5,7,9]
    for n in a:
        yield(n)
    return None

x = f1()
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
