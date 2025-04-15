class Solution:
    def countAsterisks(self, s: str) -> int:
        ret = 0
        flag = True
        for word in s.split('|'):
            if flag:
                ret += word.count('*')
            flag = not flag
        return ret
    
    def countAsterisks(self, s: str) -> int:
        ret = 0
        words = s.split('|')
        cnt = 0
        while cnt < len(words):
            ret += words[cnt].count('*')
            cnt += 2
        return ret
