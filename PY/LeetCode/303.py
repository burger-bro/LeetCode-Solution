class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


class NumArray:

    def __init__(self, nums: List[int]):
        acc = 0
        self.nums = [0]
        for n in nums:
            acc += n
            self.nums.append(acc)

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1]-self.nums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)