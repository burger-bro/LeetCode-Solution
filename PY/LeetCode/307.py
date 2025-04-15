# 线段树的节点类
class TreeNode:
    def __init__(self, val=0):
        self.left = -1                              # 区间左边界
        self.right = -1                             # 区间右边界
        self.val = val                              # 节点值（区间值）
        self.lazy_tag = None                        # 区间和问题的延迟更新标记
        
        
# 线段树类
class NumArray:
    def __init__(self, nums):
        self.size = len(nums)
        self.tree = [TreeNode() for _ in range(4 * self.size)]  # 维护 TreeNode 数组
        self.nums = nums                            # 原始数据
        self.function = lambda a, b: a+b                    # function 是一个函数，左右区间的聚合方法
        if self.size > 0:
            self.__build(0, 0, self.size - 1)
            
    # 构建线段树，节点的存储下标为 index，节点的区间为 [left, right]
    def __build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:                           # 叶子节点，节点值为对应位置的元素值
            self.tree[index].val = self.nums[left]
            return
    
        mid = left + (right - left) // 2            # 左右节点划分点
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        self.__build(left_index, left, mid)         # 递归创建左子树
        self.__build(right_index, mid + 1, right)   # 递归创建右子树
        self.__pushup(index)                        # 向上更新节点的区间值
    
    # 向上更新下标为 index 的节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果
    def __pushup(self, index):
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        self.tree[index].val = self.function(self.tree[left_index].val, self.tree[right_index].val)

    # 单点更新，将 nums[i] 更改为 val
    def update(self, i, val):
        self.nums[i] = val
        self.__update_point(i, val, 0, 0, self.size - 1)
        
    # 单点更新，将 nums[i] 更改为 val。节点的存储下标为 index，节点的区间为 [left, right]
    def __update_point(self, i, val, index, left, right):
        if self.tree[index].left == self.tree[index].right:
            self.tree[index].val = val              # 叶子节点，节点值修改为 val
            return
        
        mid = left + (right - left) // 2            # 左右节点划分点
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        if i <= mid:                                # 在左子树中更新节点值
            self.__update_point(i, val, left_index, left, mid)
        else:                                       # 在右子树中更新节点值
            self.__update_point(i, val, right_index, mid + 1, right)
        self.__pushup(index)                        # 向上更新节点的区间值

    # 区间查询，查询区间为 [q_left, q_right] 的区间值
    def sumRange(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, 0, 0, self.size - 1)
    
    # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def __query_interval(self, q_left, q_right, index, left, right):
        if left >= q_left and right <= q_right:     # 节点所在区间被 [q_left, q_right] 所覆盖
            return self.tree[index].val             # 直接返回节点值
        if right < q_left or left > q_right:        # 节点所在区间与 [q_left, q_right] 无关
            return 0
    
        self.__pushdown(index)
    
        mid = left + (right - left) // 2            # 左右节点划分点
        left_index = index * 2 + 1                  # 左子节点的存储下标
        right_index = index * 2 + 2                 # 右子节点的存储下标
        res_left = 0                                # 左子树查询结果
        res_right = 0                               # 右子树查询结果
        if q_left <= mid:                           # 在左子树中查询
            res_left = self.__query_interval(q_left, q_right, left_index, left, mid)
        if q_right > mid:                           # 在右子树中查询
            res_right = self.__query_interval(q_left, q_right, right_index, mid + 1, right)
        return self.function(res_left, res_right)   # 返回左右子树元素值的聚合计算结果























class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


class NumArray:
    def __init__(self, nums: List[int]):
        acc = 0
        self.nums = [0]
        for n in nums:
            acc += n
            self.nums.append(acc)

    def update(self, index: int, val: int) -> None:
        origin = self.sumRange(index, index)
        for i in range(index+1, len(self.nums)):
            self.nums[i] += val-origin

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1]-self.nums[left]






