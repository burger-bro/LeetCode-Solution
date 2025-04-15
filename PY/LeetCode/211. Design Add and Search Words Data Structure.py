class WordDictionary:

    def __init__(self):
        """
        优先思考search如何实现，add围绕search进一步实现
        在没有.的情况下，普通dict即可实现
        1.朴素思路：直接用dict会有什么问题？
        {.ad}当遇到通配符时，只能进行暴力查找
        另一种情况，通配符匹配已存储的通配符
        2.如果在存入通配符字符串时，
        """
        self.d = set()
        self.c_list = [chr(i) for i in range(ord('a'), ord('z')+1)] + ['.']

    def addWord(self, word: str) -> None:
        self.d.add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.d
        else:
            dot_idx = []
            for i, c in enumerate(word):
                if c == '.':
                    dot_idx.append(i)
            if len(dot_idx) == 1:
                for i in self.c_list:
                    if word[:dot_idx[0]] + i + word[dot_idx[0]+1:] in self.d:
                        return True
            elif len(dot_idx) == 2:
                for i in self.c_list:
                    for j in self.c_list:
                        if word[:dot_idx[0]] + i + word[dot_idx[0]+1:dot_idx[1]] + j + word[dot_idx[1]+1:]  in self.d:
                            return True
            return False

from itertools import combinations
class WordDictionary:

    def __init__(self):
        """
        优先思考search如何实现，add围绕search进一步实现
        在没有.的情况下，普通dict即可实现
        1.朴素思路：直接用dict会有什么问题？
        {.ad}当遇到通配符时，只能进行暴力查找
        另一种情况，通配符匹配已存储的通配符
        2.如果在存入通配符字符串时，
        """
        self.d = set()
        self.c_list = [chr(i) for i in range(ord('a'), ord('z')+1)] + ['.']

    def addWord(self, word: str) -> None:
        self.d.add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.d
        else:
            dot_idx = []
            for i, c in enumerate(word):
                if c == '.':
                    dot_idx.append(i)
            if len(dot_idx) == 1:
                for i in self.c_list:
                    if word[:dot_idx[0]] + i + word[dot_idx[0]+1:] in self.d:
                        return True
            elif len(dot_idx) == 2:
                for i in self.c_list:
                    for j in self.c_list:
                        if word[:dot_idx[0]] + i + word[dot_idx[0]+1:dot_idx[1]] + j + word[dot_idx[1]+1:]  in self.d:
                            return True
            return False

from collections import defaultdict

class TreeNode:
    def __init__(self):
        self.d = {}
        self.EOW = False

class WordDictionary:
    def __init__(self):
        """
        优先思考search如何实现，add围绕search进一步实现
        """
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.d:
                cur.d[ch] = TreeNode()
            cur = cur.d[ch]
        cur.EOW = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)

    def dfs(self, word, i, cur_node):
        if cur_node is None: return False
        if i == len(word):
            return cur_node.EOW == True
        
        if '.' == word[i]:
            return any(self.dfs(word, i+1, dd) for dd in cur_node.d.values())

        return self.dfs(word, i+1, cur_node.d.get(word[i], None))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

