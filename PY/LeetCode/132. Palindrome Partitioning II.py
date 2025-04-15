import heapq
from functools import lru_cache

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())
class Solution:
    def minCut(self, s: str) -> int:
        min_ans = float("inf")

        def is_palindrome(s):
            b, e = 0, len(s)-1
            while b <= e:
                if s[b] != s[e]:
                    return False
                b += 1
                e -= 1
            return True
        
        idx_pali_set = set()
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if is_palindrome(s[i:j]):
                    idx_pali_set.add((i, j))
        print(idx_pali_set)
        
        idx_set_dict = dict()
        for se in idx_pali_set:
            if se[0] not in idx_set_dict:
                # idx_set_dict[se[0]] = [se]
                idx_set_dict[se[0]] = [se]
            else:
                # idx_set_dict[se[0]].append(se)
                # idx_set_dict[se[0]].append(se)
                heapq.heappush(idx_set_dict[se[0]], se)
        print(idx_set_dict)

        # abbac
        # abba c
        # aabba
        # a abba
        # aabbaa

        def dfs(level, curr):
            nonlocal min_ans
            # print(level, min_ans)
            if len(curr)-1>min_ans:
                return
            if level >= len(s):
                min_ans = min(min_ans, len(curr)-1)
                return
            for se in idx_set_dict[level][::-1]:
                curr.append(se)
                dfs(se[1], curr)
                curr.pop()

        dfs(0, [])
        print(min_ans)
        return min_ans

    def minCut(self, s: str) -> int:
        @lru_cache
        def is_palindrome(s):
            b, e = 0, len(s)-1
            while b <= e:
                if s[b] != s[e]:
                    return False
                b += 1
                e -= 1
            return True
        
        @lru_cache(maxsize=1000)
        def dp(i):
            min_ans = float("inf") 
            if i == len(s):
                return 0
            for j in range(i+1, len(s)+1):
                if is_palindrome(s[i:j]):
                    min_ans = min(min_ans, dp(j)+1)
            # for j in range(i, len(s)):
            #     if is_palindrome(s[i:j+1]):
            #         min_ans = min(ans, dp(j+1)+1)
            return min_ans
        tmp = dp(0)
        print(tmp)
        return tmp - 1
    
    # def minCut(self, s: str) -> int:
    #     n = len(s)
        
    #     @lru_cache(None)
    #     def isPalindrome(l, r):  # l, r inclusive
    #         if l >= r: return True
    #         if s[l] != s[r]: return False
    #         return isPalindrome(l+1, r-1)
        
    #     @lru_cache(None)
    #     def dp(i):  # s[i..n-1]
    #         if i == n:
    #             return 0
    #         ans = float("inf") 
    #         for j in range(i, n):
    #             if (isPalindrome(i, j)):
    #                 ans = min(ans, dp(j+1) + 1)
    #         return ans
        
    #     return dp(0) - 1

su = Solution()

s = "aab"
ans = 1
res = su.minCut(s)
assert(res == ans)

s = "a"
ans = 0
res = su.minCut(s)
assert(res == ans)

s = "aa"
ans = 0
res = su.minCut(s)
assert(res == ans)

s = "aaa"
ans = 0
res = su.minCut(s)
assert(res == ans)

s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
ans = [["a","a","b"],["aa","b"]]
res = su.minCut(s)

"aabbbbba"
s = "fiefhgdcdcgfeibggchibffahiededbbegegdfibdbfdadfbdbceaadeceeefiheibahgececggaehbdcgebaigfacifhdbecbebfhiefchaaheiichgdbheacfbhfiaffaecicbegdgeiaiccghggdfggbebdaefcagihbdhhigdgbghbahhhdagbdaefeccfiaifffcfehfcdiiieibadcedibbedgfegibefagfccahfcbegdfdhhdgfhgbchiaieehdgdabhidhfeecgfiibediiafacagigbhchcdhbaigdcedggehhgdhedaebchcafcdehcffdiagcafcgiidhdhedgaaegdchibhdaegdfdaiiidcihifbfidechicighbcbgibadbabieaafgeagfhebfaheaeeibagdfhadifafghbfihehgcgggffgbfccgafigieadfehieafaehaggeeaaaehggffccddchibegfhdfafhadgeieggiigacbfgcagigbhbhefcadafhafdiegahbhccidbeeagcgebehheebfaechceefdiafgeddhdfcadfdafbhiifigcbddahbabbeedidhaieagheihhgffbfbiacgdaifbedaegbhigghfeiahcdieghhdabdggfcgbafgibiifdeefcbegcfcdihaeacihgdchihdadifeifdgecbchgdgdcifedacfddhhbcagaicbebbiadgbddcbagbafeadhddaeebdgdebafabghcabdhdgieiahggddigefddccfccibifgbfcdccghgceigdfdbghdihechfabhbacifgbiiiihcgifhdbhfcaiefhccibebcahidachfabicbdabibiachahggffiibbgchbidfbbhfcicfafgcagaaadbacddfiigdiiffhbbehaaacidggfbhgeaghigihggfcdcidbfccahhgaffiibbhidhdacacdfebedbiacaidaachegffaiiegeabfdgdcgdacfcfhdcbfiaaifgfaciacfghagceaaebhhibbieehhcbiggabefbeigcbhbcidbfhfcgdddgdffghidbbbfbdhcgabaagddcebaechbbiegeiggbabdhgghciheabdibefdfghbfbfebidhicdhbeghebeddgfdfhefebiiebdchifbcbahaddhbfafbbcebiigadhgcfbebgbebhfddgdeehhgdegaeedfadegfeihcgeefbbagbbacbgggciehdhiggcgaaicceeaefgcehfhfdciaghcbbgdihbhecfbgffefhgiefgeiggcebgaacefidghdfdhiabgibchdicdehahbibeddegfciaeaffgbefbbeihbafbagagedgbdadfdggfeaebaidchgdbcifhahgfdcehbahhdggcdggceiabhhafghegfdiegbcadgaecdcdddfhicabdfhbdiiceiegiedecdifhbhhfhgdbhibbdgafhgdcheefdhifgddchadbdggiidhbhegbdfdidhhfbehibiaacdfbiagcbheabaaebfeaeafbgigiefeaeheabifgcfibiddadicheahgbfhbhddaheghddceedigddhchecaghdegigbegcbfgbggdgbbigegffhcfcbbebdchffhddbfhhfgegggibhafiebcfgeaeehgdgbccbfghagfdbdfcbcigbigaccecfehcffahiafgabfcaefbghccieehhhiighcfeabffggfchfdgcfhadgidabdceediefdccceidcfbfiiaidechhbhdccccaigeegcaicabbifigcghcefaafaefd"
ans = [["a","a","b"],["aa","b"]]
res = su.minCut(s)