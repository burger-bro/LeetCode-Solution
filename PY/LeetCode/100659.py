class Solution:
    def maxProduct(self, n: int) -> int:
        n_str = str(n)
        n_list = []
        for c in n_str:
            n_list.append(int(c))
        n_list.sort(reverse=False)
        return n_list[0]*n_list[1]
