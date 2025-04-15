from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int =0 , nums2: List[int] =[] , n: int =0) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        1 3 5 7
        2 4 6

        1 2 5 7
        3 4 8

        1 2 3 7
        5 4 8
        ********
        1 2 5 7
        3 4 6

        1 2 3 7
        5 4 8

        5 4 2 3 7 
        """
        # print("********************start********************")
        m = len(nums1) - len(nums2)
        n = len(nums2)
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] > nums2[p2]:
                nums1[p1], nums2[p2] = nums2[p2], nums1[p1]
                # print(p2, nums2)
                if p2 < len(nums2)-1 and nums2[p2]>nums2[p2+1]:
                    # print("b", nums2)
                    tmp = p2 + 1
                    save = nums2[p2]
                    while tmp < len(nums2) and nums2[tmp] < save:
                        # print(tmp, len(nums2))
                        nums2[tmp-1] = nums2[tmp]
                        tmp += 1
                    nums2[tmp-1] = save
                    # print("a", nums2)
            p1 += 1
        for n in nums2:
            nums1[p1] = n
            p1 += 1
        return

    def merge(self, nums1: List[int], m: int =0 , nums2: List[int] =[] , n: int =0) -> None:
        m = len(nums1) - len(nums2)
        n = len(nums2)
        p, q = m-1, n-1
        cnt = m+n-1
        while cnt >= 0:
            if p >= 0 and q >= 0:
                # print("c1")
                if nums1[p] > nums2[q]:
                    nums1[cnt] = nums1[p]
                    p -= 1
                else:
                    nums1[cnt] = nums2[q]
                    q -= 1
            elif p >= 0:
                # print("c1")
                while cnt >= 0:
                    nums1[cnt] = nums1[p]
                    cnt -= 1
                    p -= 1
            elif q >= 0:
                # print("c2")
                while cnt >= 0:
                    nums1[cnt] = nums2[q]
                    cnt -= 1
                    q -= 1
            cnt -= 1
            # print(nums1, nums2)

    def merge(self, nums1: List[int], m: int =0 , nums2: List[int] =[] , n: int =0) -> None:
        m = len(nums1) - len(nums2)
        n = len(nums2)
        p, q = m-1, n-1
        cnt = m+n-1
        while q >= 0:
            if p >= 0 and nums1[p] > nums2[q]:
                nums1[cnt] = nums1[p]
                p -= 1
            else:
                nums1[cnt] = nums2[q]
                q -= 1
            cnt -= 1
            print(nums1, nums2)


su = Solution()

# case std 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
su.merge(nums1,m,nums2,n)
ans = [1,2,2,3,5,6]
assert(nums1 == ans)

# case std 2
nums1 = [1]
nums2 = []
su.merge(nums1,m,nums2,n)
ans = [1]
assert(nums1 == ans)

# case std 3
nums1 = [0]
nums2 = [1]
su.merge(nums1,m,nums2,n)
ans = [1]
assert(nums1 == ans)

"""
boundery:
len of nums1 0, 200
len of nums2 0, 200
m n
0 1
1 0
1 1
2 2
200 200
200 0
0 200
199 199

category:
[1,2,3] [4,5,6]
[1,3,5] [2,4,6]
[4,5,6] [1,2,3]
[2,4,6] [1,3,5]
[1,1,1] [2,2,2]
[1,1,3,3,5,5] [2,2,4,4,6,6,6]
"""

# case1 0 1 relate to case std3
# case2 1 0 relate to case std2
# case3 1 1
nums1 = [24242, 0]
nums2 = [34]
su.merge(nums1,m,nums2,n)
ans = [34, 24242]
assert(nums1 == ans)
# case4 1 1 inverse
nums1 = [34, 0]
nums2 = [24242]
su.merge(nums1,m,nums2,n)
ans = [34, 24242]
assert(nums1 == ans)
# case5 2 2 
nums1 = [2, 34, 0, 0]
nums2 = [1, 24242]
su.merge(nums1,m,nums2,n)
ans = [1, 2, 34, 24242]
assert(nums1 == ans)
# case5 2 2 inverse
nums1 = [2, 24242, 0, 0]
nums2 = [1, 34]
su.merge(nums1,m,nums2,n)
# print(nums1)
ans = [1, 2, 34, 24242]
assert(nums1 == ans)
# case5 2 2 inverse
nums1 = [2, 24242, 0, 0]
nums2 = [1, 34]
su.merge(nums1,m,nums2,n)
ans = [1, 2, 34, 24242]
assert(nums1 == ans)
# case6 200 200
nums1 = [1] * 100 + [0] * 100
nums2 = [2] * 100
su.merge(nums1,m,nums2,n)
ans = [1] * 100 + [2] * 100
assert(nums1 == ans)
# case7 200 0
nums1 = [1] * 100
nums2 = []
su.merge(nums1,m,nums2,n)
ans = [1] * 100
assert(nums1 == ans)
# case7 0 200
nums1 = [0] * 100
nums2 = [1] * 100
su.merge(nums1,m,nums2,n)
ans = [1] * 100
assert(nums1 == ans)
# case7 199 199 pass
nums1 = [1] * 100 + [0] * 99
nums2 = [2] * 99
su.merge(nums1,m,nums2,n)
ans = [1] * 100 + [2] * 99
assert(nums1 == ans)
# case8 123 456
nums1 = [1,2,3,0,0,0]
nums2 = [4,5,6]
su.merge(nums1,m,nums2,n)
ans = [1,2,3,4,5,6]
assert(nums1 == ans)
# case9 135 246
nums1 = [1,3,5,0,0,0]
nums2 = [2,4,6]
su.merge(nums1,m,nums2,n)
ans = [1,2,3,4,5,6]
assert(nums1 == ans)
# case10 456 123
nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]
su.merge(nums1,m,nums2,n)
# print(nums1)
ans = [1,2,3,4,5,6]
assert(nums1 == ans)
# case11 246 135
nums1 = [2,4,6,0,0,0]
nums2 = [1,3,5]
su.merge(nums1,m,nums2,n)
ans = [1,2,3,4,5,6]
assert(nums1 == ans)


print(int("100", 2))