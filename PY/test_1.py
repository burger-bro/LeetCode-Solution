# import pytest

# def sum(a, b):
#     return a + b

# class TestDemo:
#     def test_case1(self):
#         assert sum(1, 4) == 3
    
#     def test_case2(self):
#         assert sum(1, 4) == 5

# if __name__ == '__main__':
#     pytest.main()

def get_averager():
    series = []
    def averager(num):
        series.append(num)
        return sum(series)/len(series)
    return averager

avg1 = get_averager()


for i in range(10, 0, -1):
    print(i)



profits = [2,2,-3,-3,-4,5,5,5,9,-1,3,-2,-5]
merged_profits = [profits[0]]
for p in profits[1:]:
    # if last >= 0 and (p >= 0 and positive):
    #     merged_profits.pop()
    #     merged_profits.append(last+p)
    # else:
    #     positive = not positive
    #     merged_profits.append(p)
    if merged_profits[-1] * p >= 0:
        last = merged_profits.pop()
        merged_profits.append(last+p)
    else:
        merged_profits.append(p)

print(merged_profits)

a = set([1, 2])
b = set([1, 2, 3])
print(a&b)
