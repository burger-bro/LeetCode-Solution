class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg = True if numerator * denominator < 0 else False
        numerator = abs(numerator)
        denominator = abs(denominator)

        numerator = str(numerator)
        n_idx = 0
        ans = ''
        ans2 = ''

        cur_num = 0
        while True:
            twice = False
            while cur_num < denominator:
                cur_num *= 10
                flag = False
                if n_idx < len(numerator):
                    flag = True
                    cur_num += int(numerator[n_idx])
                    n_idx += 1
                elif twice:
                    if flag:
                        ans += '0'
                    else:
                        ans2 += '0'
                twice = True
            print("debug:", ans, ans2)

            div_, cur_num = divmod(cur_num, denominator)
            if flag:
                ans += str(div_)
            else:
                ans2 += str(div_)
            
            if ans2 and len(ans2) % 2 == 0:
                half = len(ans2) // 2
                if ans2[0:half] == ans2[half:]:
                    ans2 = '(' + ans2[0:half] + ')'
                    break
            if cur_num == 0: break
            print(ans, ans2)
        ret = (ans if ans else '0') + ('.'+ans2 if ans2 else '')
        print(ret)
        return -ret if neg else ret
        # 25/7 = 3 + (4/7) + ()
        
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg = True if numerator * denominator < 0 else False
        numerator = abs(numerator)
        denominator = abs(denominator)

        numerator = str(numerator)
        n_idx = 0
        ans = ''
        ans2 = ''

        cur_num = 0

        print("****************** start **********************")
        repeat_cur = {}
        loop_start = None
        while True:
            cur_num *= 10
            flag = False
            if n_idx < len(numerator):
                flag = True
                cur_num += int(numerator[n_idx])
            n_idx += 1

            print(repeat_cur, cur_num)

            if ans2 and cur_num in repeat_cur:
                loop_start = repeat_cur[cur_num]
                if ans2:
                    ans2 = ans2[:loop_start] + '(' + ans2[loop_start:] + ')'
                break
            
            div_ = ''

            if n_idx > len(numerator):
                repeat_cur[cur_num] = len(ans2)
                

            if cur_num >= denominator:
                div_, cur_num = divmod(cur_num, denominator)
            else:
                div_ = '0'

            

            if flag:
                ans += '' if (div_ == '0' and not ans) else str(div_)
            else:
                ans2 += str(div_)

            # print("debug1:", ans)
            # print("debug2:", ans2)
            if cur_num == 0 and n_idx >= len(numerator): break

            # print(ans, ans2)
        ret = (ans if ans else '0') + ('.'+ans2 if ans2 else '')
        print(ret)
        return  '-' + ret if neg else ret
        # 25/7 = 3 + (4/7) + ()

su = Solution()

numerator = 420
denominator = 226
ans = "1.(8584070796460176991150442477876106194690265486725663716814159292035398230088495575221238938053097345132743362831)"
res = su.fractionToDecimal(numerator, denominator)
assert(res == ans)
# exit(0)

numerator = 666
denominator = 1000
ans = "0.666"
res = su.fractionToDecimal(numerator, denominator)
assert(res == ans)


numerator = 1
denominator = 6
ans = "0.1(6)"
res = su.fractionToDecimal(numerator, denominator)
# assert(res == ans)


numerator = 172
denominator = 23
ans = "7.(4782608695652173913043)"
res = su.fractionToDecimal(numerator, denominator)
assert(res == ans)
# exit(0)

numerator = 1
denominator = 2
ans = "0.5"
res = su.fractionToDecimal(numerator, denominator)
assert(res == ans)

numerator = 2
denominator = 1
ans = "2"
res = su.fractionToDecimal(numerator, denominator)
assert(res == ans)


numerator = 4
denominator = 333
ans = "0.(012)"
res = su.fractionToDecimal(numerator, denominator)
assert(res == ans)
exit(0)
