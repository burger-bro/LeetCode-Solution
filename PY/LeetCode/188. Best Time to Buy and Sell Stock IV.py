from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        profits = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        merged_profits = [profits[0]]

        # 合并连正连负
        for p in profits[1:]:
            if merged_profits[-1] * p >= 0:
                last = merged_profits.pop()
                merged_profits.append(last+p)
            else:
                merged_profits.append(p)

        ans = 0 

        # 剔除首尾负值
        sorted_profits = sorted(merged_profits, reverse=True)
        for i in range(len(sorted_profits)):
            if sorted_profits[i] < 0: break
            ans += sorted_profits[i]
            if i == k - 1: break


        # print(ans)
        left, right = 0, -1
        for l in range(len(merged_profits)):
            if merged_profits[l] > 0:
                left = l
                break
        for r in range(len(merged_profits)-1, -1,-1):
            if merged_profits[r] > 0:
                right = r
                break
        splited_merged_profits = merged_profits[left:right+1]
        print("split:", splited_merged_profits)

        # 合并三数
        # i1, i2, i3 = 0, 1, 2
        # while i1 < len(splited_merged_profits) and i2 < len(splited_merged_profits) and i3 < len(splited_merged_profits):
        #     if splited_merged_profits[i1] + splited_merged_profits[i2] + splited_merged_profits[i3] >= max(splited_merged_profits[i1], splited_merged_profits[i3]):
        #         new_tmp = splited_merged_profits[i1] + splited_merged_profits[i2] + splited_merged_profits[i3]
        #         del splited_merged_profits[i1]
        #         del splited_merged_profits[i1]
        #         del splited_merged_profits[i1]
        #         splited_merged_profits.insert(i1, new_tmp)
        #         i1, i2, i3 = 0, 1, 2
        #     else:
        #         i1 += 3
        #         i2 += 3
        #         i3 += 3
        # print("split2:", splited_merged_profits)

        def dfs(index, cur_sum, pos_cnt, merge=None):
            nonlocal ans
            if pos_cnt > k:
                return
            else:
                ans = max(ans, cur_sum)

            if index > len(splited_merged_profits) - 1:
                return
            
            tmp_i = index + 1
            tmp_sum = splited_merged_profits[index]
            while tmp_i < len(splited_merged_profits) and splited_merged_profits[tmp_i] < 0:
                tmp_sum += splited_merged_profits[tmp_i]
                tmp_i += 1
            if tmp_i != index:
                # 直接相加
                dfs(tmp_i, cur_sum+splited_merged_profits[index], pos_cnt+1) # tmp_i > 0 ???
                if merge is not None:
                    dfs(tmp_i, cur_sum+splited_merged_profits[index]+merge, pos_cnt+1)
            if tmp_i < len(splited_merged_profits):
                # 合并相加
                dfs(tmp_i, cur_sum, pos_cnt, tmp_sum)
                if merge is not None:
                    dfs(tmp_i, cur_sum, pos_cnt, merge+tmp_sum)
            # 跳过
            dfs(tmp_i, cur_sum, pos_cnt)

        dfs(0, 0, 0)
        print("ans", ans)
        # max(merge_positive_num_to_k())


        # ans = 0
        # for i in range(len(merged_profits)):
        #     if merged_profits[i] < 0: break
        #     ans += merged_profits[i]
        #     if i == k - 1: break


        return ans

from typing import List

class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

def build_list(array):
    dummy = Node()
    prev = dummy
    for n in array:
        cur = Node(n)
        cur.prev = prev
        prev.next = cur
        prev = cur
    dummy.next.prev = None
    return dummy.next

def print_list(head):
    n = head
    while n is not None:
        print(n.val, end=',')
        n = n.next
    print('')

# a = [1]
# a = [1,3,5,7,9,]
# a = build_list(a)
# print_list(a)
# exit(0)

class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0

        variants = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        if len(variants) == 1: return variants[0] if variants[0] > 0 else 0
        m = len(prices)
        max_profits_ends_with = [0]*m
        max_profits_starts_with = [0]*m
        for i in range(1, m):
            max_profits_ends_with[i] = max(variants[i-1], variants[i-1]+max_profits_ends_with[i-1])
        max_profits_ends_with.pop(0)
        for i in range(m-2, -1, -1):
            max_profits_starts_with[i] = max(variants[i], variants[i]+max_profits_starts_with[i+1])
        max_profits_starts_with.pop()

        for i in range(1, len(variants)):
            max_profits_ends_with[i] = max(max_profits_ends_with[i-1], max_profits_ends_with[i])

        for i in range(len(variants)-2, -1, -1):
            max_profits_starts_with[i] = max(max_profits_starts_with[i+1], max_profits_starts_with[i])
  
        ret = 0
        
        for i in range(0, len(variants)-1):
            ret = max(ret, max_profits_ends_with[i]+max_profits_starts_with[i+1])
        return max([ret, max_profits_ends_with[m-2], max_profits_starts_with[0]])

    def maxProfit(self, k: int, prices: List[int]) -> int:
        print("************************ start *************************")
        # if k == 2: return self.maxProfit2(prices)
        if len(prices) == 1: return 0
        profits = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        merged_profits = [profits[0]]

        # 合并连正连负
        for p in profits[1:]:
            if merged_profits[-1] * p >= 0:
                last = merged_profits.pop()
                merged_profits.append(last+p)
            else:
                merged_profits.append(p)

        ans = 0 

        # 剔除首尾负值
        sorted_profits = sorted(merged_profits, reverse=True)
        for i in range(len(sorted_profits)):
            if sorted_profits[i] < 0: break
            ans += sorted_profits[i]
            if i == k - 1: break


        # print(ans)
        left, right = 0, -1
        for l in range(len(merged_profits)):
            if merged_profits[l] > 0:
                left = l
                break
        for r in range(len(merged_profits)-1, -1,-1):
            if merged_profits[r] > 0:
                right = r
                break
        splited_merged_profits = merged_profits[left:right+1]
        print("split:", splited_merged_profits)

        positive, negative = [], []
        for n in splited_merged_profits:
            if n > 0:
                positive.append(n)
            else:
                negative.append(n)
        print("pon", positive, negative)

        cur_ans = 0 
        # print("kl", k, len(positive))
        if len(positive) <= k:
            cur_ans = sum(positive)
        else:
            # # method1
            negative.sort(reverse=True)
            positive.sort(reverse=True)
            # case1
            ans = sum(positive)
            print("ans1", ans)
            for n in range(len(positive)-k):
                ans += negative[n]
            print("ans1", ans)
            # case2
            ans2 = 0
            for n in range(k):
                ans2 += positive[n]
            print("ans2", ans2)
            cur_ans = max(ans, ans2)

            # method2
            # 合并的亏损是negative[n]，拿不到的亏损是positive[n]
            # 更一般的情况是，合并一些，再拿最大的。而不是m1中的要么全合并，要么只拿最大
            # 所以关键问题在于，怎么判断哪些该合并？
            # 或者换一种说法，哪一种操作是一定不亏的？
            # 思路1：当还剩余len(positve)-k次合并机会时，尝试找最优合并
            # 如何定义最优合并？ 亏损的合并neg+min(pos1,pos2)<0
            # 所以是否可以定义neg+min(pos1, pos2)>=0为最大的那些合并为最优合并？
            # 问题1：有没有办法处理连续多次合并？ (5 -1 2 -4 5) (6 -1 2 -4 5)
            # 思路2：比较max(pos)和neg(min)，如果拿了max，则相当于亏损了min(pos)
            #       或者执行另一个操作即合并，此时赚neg+min(pos1,pos2)
            # 问题2：为什么有时直接取max_sum(pos, k)即可，而有时还需要合并
            # 原因：因为需要合并的那些情况下，可以构造出更大的值使其位于max_sum中，从而增加总利润
            # 执行合并总是赚的吗？会不会有亏损？ (21,-3,8,-1,10,-5,9)
            # 构造双链表，执行k次最优合并

            # dummy_head = Node()
            # head = build_list(splited_merged_profits)
            # dummy_head.next = head
            # head.prev = dummy_head

            # merge_num = len(positive)-k

            # def get_ans(n):
            #     ans_list = []
            #     while n is not None:
            #         if n.val > 0:
            #             ans_list.append(n.val)
            #         n = n.next
                
            #     ans_list.sort(reverse=True)
            #     ans = 0
            #     for i in range(min(k, len(ans_list))):
            #         ans += ans_list[i]
            #     return ans

            # while merge_num:
            #     max_profit_merge_node = None
            #     limit = -200
            #     max_profit_val = limit-1
            #     n = dummy_head.next
            #     while n is not None:
            #         if n.val > 0:
            #             n = n.next
            #             continue
            #         profit = n.val + min(n.prev.val, n.next.val)
            #         if profit >= limit and profit >= max_profit_val: # modify
            #             max_profit_val = profit
            #             max_profit_merge_node = n
            #         n = n.next
            #     if max_profit_val >= limit: # modify
            #         merge_num -= 1
            #     else:
            #         print("break?")
            #         print(max_profit_val)
            #         print_list(dummy_head)
            #         print("down")
            #         break
            #     print("cur", max_profit_merge_node.val)
            #     mp = max_profit_merge_node
            #     prev_ = max_profit_merge_node.prev.prev
            #     next_ = max_profit_merge_node.next.next
            #     new_node = Node(mp.val+mp.prev.val+mp.next.val, prev_, next_)
            #     prev_.next = new_node
            #     if next_ is not None:
            #         next_.prev = new_node
            #     # print("******debug1*****")
            #     # print_list(dummy_head.next)
            #     # print("******debug1*****")
            #     cur_ans = max(get_ans(dummy_head.next), cur_ans)
            # print("3")
            # cur_ans = max(get_ans(dummy_head.next), cur_ans)

            # # print("******debug*****")
            # # print_list(dummy_head)
            # # print("******debug*****")


            # ans = get_ans(n)

        print("ans", cur_ans)

        return cur_ans

su = Solution()



# debug

k = 29
prices = [70,4,83,56,94,72,78,43,2,86,65,100,94,56,41,66,3,33,10,3,45,94,15,12,78,60,58,0,58,15,21,7,11,41,12,96,83,77,47,62,27,19,40,63,30,4,77,52,17,57,21,66,63,29,51,40,37,6,44,42,92,16,64,33,31,51,36,0,29,95,92,35,66,91,19,21,100,95,40,61,15,83,31,55,59,84,21,99,45,64,90,25,40,6,41,5,25,52,59,61,51,37,92,90,20,20,96,66,79,28,83,60,91,30,52,55,1,99,8,68,14,84,59,5,34,93,25,10,93,21,35,66,88,20,97,25,63,80,20,86,33,53,43,86,53,55,61,77,9,2,56,78,43,19,68,69,49,1,6,5,82,46,24,33,85,24,56,51,45,100,94,26,15,33,35,59,25,65,32,26,93,73,0,40,92,56,76,18,2,45,64,66,64,39,77,1,55,90,10,27,85,40,95,78,39,40,62,30,12,57,84,95,86,57,41,52,77,17,9,15,33,17,68,63,59,40,5,63,30,86,57,5,55,47,0,92,95,100,25,79,84,93,83,93,18,20,32,63,65,56,68,7,31,100,88,93,11,43,20,13,54,34,29,90,50,24,13,44,89,57,65,95,58,32,67,38,2,41,4,63,56,88,39,57,10,1,97,98,25,45,96,35,22,0,37,74,98,14,37,77,54,40,17,9,28,83,13,92,3,8,60,52,64,8,87,77,96,70,61,3,96,83,56,5,99,81,94,3,38,91,55,83,15,30,39,54,79,55,86,85,32,27,20,74,91,99,100,46,69,77,34,97,0,50,51,21,12,3,84,84,48,69,94,28,64,36,70,34,70,11,89,58,6,90,86,4,97,63,10,37,48,68,30,29,53,4,91,7,56,63,22,93,69,93,1,85,11,20,41,36,66,67,57,76,85,37,80,99,63,23,71,11,73,41,48,54,61,49,91,97,60,38,99,8,17,2,5,56,3,69,90,62,75,76,55,71,83,34,2,36,56,40,15,62,39,78,7,37,58,22,64,59,80,16,2,34,83,43,40,39,38,35,89,72,56,77,78,14,45,0,57,32,82,93,96,3,51,27,36,38,1,19,66,98,93,91,18,95,93,39,12,40,73,100,17,72,93,25,35,45,91,78,13,97,56,40,69,86,69,99,4,36,36,82,35,52,12,46,74,57,65,91,51,41,42,17,78,49,75,9,23,65,44,47,93,84,70,19,22,57,27,84,57,85,2,61,17,90,34,49,74,64,46,61,0,28,57,78,75,31,27,24,10,93,34,19,75,53,17,26,2,41,89,79,37,14,93,55,74,11,77,60,61,2,68,0,15,12,47,12,48,57,73,17,18,11,83,38,5,36,53,94,40,48,81,53,32,53,12,21,90,100,32,29,94,92,83,80,36,73,59,61,43,100,36,71,89,9,24,56,7,48,34,58,0,43,34,18,1,29,97,70,92,88,0,48,51,53,0,50,21,91,23,34,49,19,17,9,23,43,87,72,39,17,17,97,14,29,4,10,84,10,33,100,86,43,20,22,58,90,70,48,23,75,4,66,97,95,1,80,24,43,97,15,38,53,55,86,63,40,7,26,60,95,12,98,15,95,71,86,46,33,68,32,86,89,18,88,97,32,42,5,57,13,1,23,34,37,13,65,13,47,55,85,37,57,14,89,94,57,13,6,98,47,52,51,19,99,42,1,19,74,60,8,48,28,65,6,12,57,49,27,95,1,2,10,25,49,68,57,32,99,24,19,25,32,89,88,73,96,57,14,65,34,8,82,9,94,91,19,53,61,70,54,4,66,26,8,63,62,9,20,42,17,52,97,51,53,19,48,76,40,80,6,1,89,52,70,38,95,62,24,88,64,42,61,6,50,91,87,69,13,58,43,98,19,94,65,56,72,20,72,92,85,58,46,67,2,23,88,58,25,88,18,92,46,15,18,37,9,90,2,38,0,16,86,44,69,71,70,30,38,17,69,69,80,73,79,56,17,95,12,37,43,5,5,6,42,16,44,22,62,37,86,8,51,73,46,44,15,98,54,22,47,28,11,75,52,49,38,84,55,3,69,100,54,66,6,23,98,22,99,21,74,75,33,67,8,80,90,23,46,93,69,85,46,87,76,93,38,77,37,72,35,3,82,11,67,46,53,29,60,33,12,62,23,27,72,35,63,68,14,35,27,98,94,65,3,13,48,83,27,84,86,49,31,63,40,12,34,79,61,47,29,33,52,100,85,38,24,1,16,62,89,36,74,9,49,62,89]
ans = 5
res = su.maxProfit(k, prices)
assert(res == ans)
exit(0)


# debug

k = 1
prices = [6,1,6,4,3,0,2]
ans = 5
res = su.maxProfit(k, prices)
assert(res == ans)
exit(0)


# debug

k = 2
prices = [2,6,8,7,8,7,9,4,1,2,4,5,8]
ans = 14
res = su.maxProfit(k, prices)
assert(res == ans)
exit(0)

# debug

k = 2
prices = [6,5,4,8,6,8,7,8,9,4,5]
ans = 7
res = su.maxProfit(k, prices)
assert(res == ans)
# exit(0)

k = 2
prices = [2,4,1]
ans = 2
res = su.maxProfit(k, prices)
assert(res == ans)

k = 2
prices = [3,2,6,5,0,3]
su.maxProfit(k, prices) # 7
ans = 7
res = su.maxProfit(k, prices)
assert(res == ans)

k = 2
prices = [3,2,6,5,9,3] # 8
su.maxProfit(k, prices)
ans = 8
res = su.maxProfit(k, prices)
assert(res == ans)

k = 2
prices = [3,2,6,7,9,3] # 7
su.maxProfit(k, prices)
ans = 7
res = su.maxProfit(k, prices)
assert(res == ans)


k = 2
prices = [3,3,5,0,0,3,1,4]
su.maxProfit(k, prices)
ans = 6
res = su.maxProfit(k, prices)
assert(res == ans)

k = 2
prices = [1,2,4,2,5,7,2,4,9,0]
su.maxProfit(k, prices)
ans = 13
res = su.maxProfit(k, prices)
assert(res == ans)

k = 2
prices = [1,2,4,2,5,7,2,4,9,0,9] # 17
ans = 17
res = su.maxProfit(k, prices)
assert(res == ans)

k = 2
prices = [4,1,2,4,2,5,7,2,4,9,0] # 13
su.maxProfit(k, prices)
ans = 13
res = su.maxProfit(k, prices)
assert(res == ans)

k = 2
prices = [5,2,3,2,6,6,2,9,1,0,7,4,5,0] # 14
su.maxProfit(k, prices)
ans = 14
res = su.maxProfit(k, prices)
assert(res == ans)

# k = 2
# prices = [5,4,3,2,1,0]
# su.maxProfit(k, prices)


# k = 29
# prices = [70,4,83,56,94,72,78,43,2,86,65,100,94,56,41,66,3,33,10,3,45,94,15,12,78,60,58,0,58,15,21,7,11,41,12,96,83,77,47,62,27,19,40,63,30,4,77,52,17,57,21,66,63,29,51,40,37,6,44,42,92,16,64,33,31,51,36,0,29,95,92,35,66,91,19,21,100,95,40,61,15,83,31,55,59,84,21,99,45,64,90,25,40,6,41,5,25,52,59,61,51,37,92,90,20,20,96,66,79,28,83,60,91,30,52,55,1,99,8,68,14,84,59,5,34,93,25,10,93,21,35,66,88,20,97,25,63,80,20,86,33,53,43,86,53,55,61,77,9,2,56,78,43,19,68,69,49,1,6,5,82,46,24,33,85,24,56,51,45,100,94,26,15,33,35,59,25,65,32,26,93,73,0,40,92,56,76,18,2,45,64,66,64,39,77,1,55,90,10,27,85,40,95,78,39,40,62,30,12,57,84,95,86,57,41,52,77,17,9,15,33,17,68,63,59,40,5,63,30,86,57,5,55,47,0,92,95,100,25,79,84,93,83,93,18,20,32,63,65,56,68,7,31,100,88,93,11,43,20,13,54,34,29,90,50,24,13,44,89,57,65,95,58,32,67,38,2,41,4,63,56,88,39,57,10,1,97,98,25,45,96,35,22,0,37,74,98,14,37,77,54,40,17,9,28,83,13,92,3,8,60,52,64,8,87,77,96,70,61,3,96,83,56,5,99,81,94,3,38,91,55,83,15,30,39,54,79,55,86,85,32,27,20,74,91,99,100,46,69,77,34,97,0,50,51,21,12,3,84,84,48,69,94,28,64,36,70,34,70,11,89,58,6,90,86,4,97,63,10,37,48,68,30,29,53,4,91,7,56,63,22,93,69,93,1,85,11,20,41,36,66,67,57,76,85,37,80,99,63,23,71,11,73,41,48,54,61,49,91,97,60,38,99,8,17,2,5,56,3,69,90,62,75,76,55,71,83,34,2,36,56,40,15,62,39,78,7,37,58,22,64,59,80,16,2,34,83,43,40,39,38,35,89,72,56,77,78,14,45,0,57,32,82,93,96,3,51,27,36,38,1,19,66,98,93,91,18,95,93,39,12,40,73,100,17,72,93,25,35,45,91,78,13,97,56,40,69,86,69,99,4,36,36,82,35,52,12,46,74,57,65,91,51,41,42,17,78,49,75,9,23,65,44,47,93,84,70,19,22,57,27,84,57,85,2,61,17,90,34,49,74,64,46,61,0,28,57,78,75,31,27,24,10,93,34,19,75,53,17,26,2,41,89,79,37,14,93,55,74,11,77,60,61,2,68,0,15,12,47,12,48,57,73,17,18,11,83,38,5,36,53,94,40,48,81,53,32,53,12,21,90,100,32,29,94,92,83,80,36,73,59,61,43,100,36,71,89,9,24,56,7,48,34,58,0,43,34,18,1,29,97,70,92,88,0,48,51,53,0,50,21,91,23,34,49,19,17,9,23,43,87,72,39,17,17,97,14,29,4,10,84,10,33,100,86,43,20,22,58,90,70,48,23,75,4,66,97,95,1,80,24,43,97,15,38,53,55,86,63,40,7,26,60,95,12,98,15,95,71,86,46,33,68,32,86,89,18,88,97,32,42,5,57,13,1,23,34,37,13,65,13,47,55,85,37,57,14,89,94,57,13,6,98,47,52,51,19,99,42,1,19,74,60,8,48,28,65,6,12,57,49,27,95,1,2,10,25,49,68,57,32,99,24,19,25,32,89,88,73,96,57,14,65,34,8,82,9,94,91,19,53,61,70,54,4,66,26,8,63,62,9,20,42,17,52,97,51,53,19,48,76,40,80,6,1,89,52,70,38,95,62,24,88,64,42,61,6,50,91,87,69,13,58,43,98,19,94,65,56,72,20,72,92,85,58,46,67,2,23,88,58,25,88,18,92,46,15,18,37,9,90,2,38,0,16,86,44,69,71,70,30,38,17,69,69,80,73,79,56,17,95,12,37,43,5,5,6,42,16,44,22,62,37,86,8,51,73,46,44,15,98,54,22,47,28,11,75,52,49,38,84,55,3,69,100,54,66,6,23,98,22,99,21,74,75,33,67,8,80,90,23,46,93,69,85,46,87,76,93,38,77,37,72,35,3,82,11,67,46,53,29,60,33,12,62,23,27,72,35,63,68,14,35,27,98,94,65,3,13,48,83,27,84,86,49,31,63,40,12,34,79,61,47,29,33,52,100,85,38,24,1,16,62,89,36,74,9,49,62,89]
# su.maxProfit(k, prices)
