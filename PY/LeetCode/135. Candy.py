from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        print("******************start*******************")
        min_r = min(ratings)
        start = ratings.index(min_r)
        print(start)
        candy_num = 1

        def get_one_side(_range, _compare):
            nonlocal candy_num
            cur = 1
            stack = []
            last_ascend_val = float("inf")
            last_ascend_idx = -1
            for i in _range:
                print("round candy", candy_num)
                if _compare(i):
                    if stack:
                        print("stack", stack)
                        cur = 1
                        last = float("inf")
                        for s in stack[::-1]:
                            if s > last:
                                cur += 1
                            elif s == last:
                                cur = 1
                            last = s
                            candy_num += cur
                        print("after stack", candy_num)
                        if cur >= last_ascend_val:
                            if last_ascend_rating > stack[0]:
                                candy_num += cur - last_ascend_val + 1
                        stack = []
                        cur = 1
                    cur += 1
                    candy_num += cur
                    last_ascend_val = cur
                    last_ascend_rating = ratings[i]
                else:
                    stack.append(ratings[i])

            if stack:
                print("stack", stack)
                cur = 1
                last = float("inf")
                for s in stack[::-1]:
                    if s > last:
                        cur += 1
                    elif s == last:
                        cur = 1
                    last = s
                    candy_num += cur
                if cur >= last_ascend_val:
                    if last_ascend_rating > stack[0]:
                        candy_num += cur - last_ascend_val + 1
            # print("after right", candy_num)

        range1 = range(start+1, len(ratings))
        range2 = range(start-1, -1, -1)
        compare1 = lambda i: ratings[i]>ratings[i-1]
        compare2 = lambda i: ratings[i]>ratings[i+1]
        get_one_side(range1, compare1)
        get_one_side(range2, compare2)
    
        print("candy_num", candy_num)
        return candy_num

    def candy(self, ratings: List[int]) -> int:
        print("******************start*******************")
        
        ratings.insert(0, -1)
        candy_num = 0

        cur = 0
        stack = []
        last_ascend_val = float("inf")
        for i in range(1, len(ratings)):
            print("round candy", candy_num)
            if ratings[i]>ratings[i-1]:
                if stack:
                    print("stack", stack)
                    cur = 1
                    last = float("inf")
                    for s in stack[::-1]:
                        if s > last:
                            cur += 1
                        elif s == last:
                            cur = 1
                        last = s
                        candy_num += cur
                    print("after stack", candy_num)
                    if cur >= last_ascend_val:
                        if last_ascend_rating > stack[0]:
                            candy_num += cur - last_ascend_val + 1
                    stack = []
                    cur = 1
                cur += 1
                candy_num += cur
                last_ascend_val = cur
                last_ascend_rating = ratings[i]
            else:
                stack.append(ratings[i])

        if stack:
            print("stack", stack)
            cur = 1
            last = float("inf")
            for s in stack[::-1]:
                if s > last:
                    cur += 1
                elif s == last:
                    cur = 1
                last = s
                candy_num += cur
            if cur >= last_ascend_val:
                if last_ascend_rating > stack[0]:
                    candy_num += cur - last_ascend_val + 1

        print("candy_num", candy_num)
        return candy_num

su = Solution()

# case bug4
ratings = [29,51,87,87,72,12]
# 1 2 3 (3 2 1)
res = su.candy(ratings)
ans = 12
assert(res == ans)

# case bug3
ratings = [1,2,3,5,4,3,2,1]
# 1 2 3 4 (4 3 2 1)
res = su.candy(ratings)
ans = 21
assert(res == ans)

# case bug2
ratings = [1,6,10,8,7,3,2]
# 1 2 3 (4 3 2 1)
res = su.candy(ratings)
ans = 18
assert(res == ans)

# case bug
ratings = [1,3,2,2,1]
# 1 2 1 2 1
# 1 3 2 2 1
res = su.candy(ratings)
ans = 7
assert(res == ans)

# std1
ratings = [1,0,2]
# min_id = 1 ratings[min_id] = 1 
# 1 2 3 2 2 1 0 3 4 1 0 2 3
# x x x x x x 1 x x x x x x 
# x x x x x 2 1 2 x x x x x 
# x x x x 3 2 1 2 3 x x x x 
# x x ? 2 3 2 1 2 3 ? x x x 如果发现相等的，就分配为小1的？或者0？
# x ? ? 2 3 2 1 2 3 ? x x x 
# x x x x x x 1 x x x x x x 

# 1 0 1 2     2       1      1        3
# 2 1 2 3  n(<=3)    n-1   m(m<=n)   m+1
# 2 1 2 3 2 1 1 2
# 从最小的出发，将它置为1，然后往左右继续找
# 如果下一个值大于当前值，则+1。如果下一个值小于等于当前值？
# 如何处理小于和等于的情况？
# 将ratings看作连续的山脉，求解过程可以抽象为，先把所有山谷的值设为0，
# 然后每爬一格，山的高度加一，求所有位置山高的总和。 平地、高原如何处理？
res = su.candy(ratings)
ans = 5
assert(res == ans)
# exit(0)

# std2
ratings = [1,2,2] 
res = su.candy(ratings)
ans = 4
assert(res == ans)

# case1
ratings = [1,0,1,2,2,1,1,3] 
res = su.candy(ratings)
ans = 14
assert(res == ans)

# case2 reverse
ratings = [1,0,1,2,2,1,1,3]
ratings.reverse()
res = su.candy(ratings)
ans = 14
assert(res == ans)

# case3
ratings = [1,0,2,3,3,3,3,3]
# 2 1 2 3 3 3 3 3
# 2 1 2 3 1 1 1 1
ratings.reverse()
res = su.candy(ratings)
ans = 12
assert(res == ans)

# case4
ratings = [0,0,0,0,0,0]
res = su.candy(ratings)
ans = 6
assert(res == ans)

# case5
ratings = [1,4,4,4,2,2,3,3,3]
# 1 2 1 2 1 1 2 1 1
res = su.candy(ratings)
ans = 12
assert(res == ans)
