from typing import List
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 注意到规则2，加上一个K其实并没有什么实际意义。
        # 如果能找到nums中原本频数最大的两个数，则答案就是两数之一
        # 问题在于如何选择子数组，只有子数组内的数值可以这样操作。
        # 1 1 1 2 3 2 1 1 1 1 (2) -> [0, -1] +1

        def max_f(arr):
            cnt = 0
            candidate = None
            target_num = 0
            for n in arr:
                if n == k:
                    target_num += 1
                if cnt == 0:
                    candidate = n
                if candidate == n:
                    cnt += 1
                else:
                    cnt -= 1
            return candidate, target_num, candidate

        def get_f(arr, t):
            cnt = 0
            for n in arr:
                if n == t:
                    cnt += 1
            return cnt

        print("*********** start ************")
        ans = -1

        glb_d = Counter(nums)
        print(glb_d)

        cur_tar = glb_d[k]

        length = len(nums)
        for i in range(length):
            for j in range(i+1, length+1):
                candi, tar, debug = max_f(nums[i:j])
                candi = get_f(nums[i:j], candi)
                tmp = (cur_tar - tar) + candi
                if tmp > ans:
                    ans = tmp
        print(ans)
        return ans

    def maxFrequency(self, nums: List[int], k: int) -> int:
        def max_f(arr):
            tmp_d = {}
            max_freq = 0
            for n in arr:
                tmp_d[n] = tmp_d.get(n, 0) + 1
                max_freq = max(tmp_d[n], max_freq)

            return max_freq, tmp_d.get(k, 0)

        print("*********** start ************")
        ans = -1

        glb_d = Counter(nums)
        print(glb_d)

        cur_tar = glb_d[k]

        length = len(nums)
        for i in range(length):
            for j in range(i+1, length+1):
                candi, tar = max_f(nums[i:j])
                tmp = (cur_tar - tar) + candi
                if tmp > ans:
                    ans = tmp
        print(ans)
        return ans

    def maxFrequency(self, nums: List[int], k: int) -> int:
            print("*********** start ************")
            ans = -1

            glb_d = Counter(nums)
            print(glb_d)

            cur_tar = glb_d[k]

            length = len(nums)
            for i in range(length):
                tmp_d = {}
                max_freq = 0
                for j in range(i, length):
                    tmp_d[nums[j]] = tmp_d.get(nums[j], 0) + 1
                    max_freq = max(tmp_d[nums[j]], max_freq)

                    candi, tar = max_freq, tmp_d.get(k, 0)
                    tmp = (cur_tar - tar) + candi
                    if tmp > ans:
                        ans = tmp
            print(ans)
            return ans

    def maxFrequency(self, nums: List[int], k: int) -> int:
            print("*********** start ************")
            glb_k = nums.count(k)

            print("glb", glb_k)
            ans = 0
            for i in range(1, 51):
                max_freq = 0
                cur_freq = 0
                for n in nums:
                    if n == k:
                        cur_freq -= 1
                    elif n == i:
                        cur_freq += 1
                    cur_freq = max(cur_freq, 0)
                    max_freq = max(cur_freq, max_freq)
                # print("i", i, max_freq)
                ans = max(ans, max_freq)

            print("ans", ans)
            return ans + glb_k

su = Solution()

# case std1
nums = [1,2,3,4,5,6]
k = 1
res = su.maxFrequency(nums, k)
ans = 2
assert(res == ans)

# case std2
nums = [10,2,3,4,5,5,4,3,2,2]
k = 10
res = su.maxFrequency(nums, k)
ans = 4
assert(res == ans)

# case1
nums = [2,2,2,2]
k = 2
res = su.maxFrequency(nums, k)
ans = 4
assert(res == ans)

# case1
nums = [2]
k = 2
res = su.maxFrequency(nums, k)
ans = 1
assert(res == ans)

# case2
nums = [2]
k = 1
res = su.maxFrequency(nums, k)
ans = 1
assert(res == ans)

# case3
nums = [2,3,4,5,3,3,3]*10000
k = 2
res = su.maxFrequency(nums, k)
# ans = 4
# assert(res == ans)
