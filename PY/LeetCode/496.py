from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        for q in nums1:
            idx = nums2.index(q)
            for i in range(idx+1, len(nums2)):
                if nums2[i] > q:
                    ret.append(nums2[i])
                    break
            else:
                ret.append(-1)
        print(ret)
        return ret

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        for i, n in enumerate(nums1):
            nums1_dict[n] = i
        nums1.sort()
        ret = [None]*len(nums1)
        stack = []

        return ret

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        nums_dict = {n:-1 for n in nums1}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                if stack[-1] in nums_dict:
                    nums_dict[stack[-1]] = n
                stack.pop()
            stack.append(n)
        return [nums_dict[n] for n in nums1]

su = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
res = su.nextGreaterElement(nums1, nums2)
ans = [-1, 3, -1]
assert(res == ans)


