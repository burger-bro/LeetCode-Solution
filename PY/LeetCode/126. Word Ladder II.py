from typing import List
from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def diff_one(word1, word2):
            diff_cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_cnt += 1
            return diff_cnt == 1
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return []

        graph = [[False]*len(wordList) for _ in range(len(wordList))]
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                graph[i][j] = diff_one(wordList[i], wordList[j])
        # print(graph)

        queue = deque([(wordList.index(beginWord), [beginWord], set([wordList.index(beginWord)]))])
        target_idx = wordList.index(endWord)
        shortest = float("inf")
        ret_list = []
        while queue:
            cur_idx, cur_ans, visited = queue.popleft()
            # print(cur_idx)
            print(shortest, cur_ans, visited)
            if cur_idx == target_idx:
                shortest = min(shortest, len(cur_ans))
                if len(cur_ans) == shortest:
                    ret_list.append(cur_ans)
            if len(cur_ans) >= shortest:
                continue
            for j in range(len(wordList)):
                if graph[cur_idx][j] and j not in visited:
                    new_visited = visited.copy()
                    new_visited.add(j)
                    queue.append((j, cur_ans+[wordList[j]], new_visited))
        print(ret_list)
        return ret_list

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def diff_one(word1, word2):
            diff_cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_cnt += 1
            return diff_cnt == 1
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return []

        graph = [[False]*len(wordList) for _ in range(len(wordList))]
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                graph[i][j] = diff_one(wordList[i], wordList[j])

        queue = deque([[wordList.index(beginWord)]])
        target_idx = wordList.index(endWord)
        shortest = float("inf")
        ret_list = []
        while queue:
            cur_ans_idx = queue.popleft()
            cur_idx = cur_ans_idx[-1]
            # print(cur_idx)
            print(shortest, cur_ans_idx, cur_idx)

            if cur_idx == target_idx:
                shortest = min(shortest, len(cur_ans_idx))
                if len(cur_ans_idx) == shortest:
                    tmp = [wordList[i] for i in cur_ans_idx]
                    ret_list.append(tmp)
            if len(cur_ans_idx) >= shortest:
                continue
            flag = True
            for j in range(len(wordList)):
                if graph[cur_idx][j] and j not in cur_ans_idx:
                    flag = False
                    # queue.append((cur_ans_idx+[j]))
                    cur_ans_idx.append(j)
                    queue.append((cur_ans_idx.copy()))
                    # for i in range(len(wordList)):
                    #     graph[i][j] = False
            if flag:
                for i in range(len(wordList)):
                    graph[i][cur_idx] = False
        print(ret_list)
        return ret_list

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def diff_one(word1, word2):
            diff_cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_cnt += 1
            return diff_cnt == 1
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return []

        graph = [[False]*len(wordList) for _ in range(len(wordList))]
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                graph[i][j] = diff_one(wordList[i], wordList[j])

        queue = deque([[wordList.index(beginWord)]])
        target_idx = wordList.index(endWord)
        shortest = float("inf")
        ret_list = []
        while queue:
            tmp_delete_list = []
            print("len(queue):", len(queue))
            for _ in range(len(queue)):
                cur_ans_idx = queue.popleft()
                cur_idx = cur_ans_idx[-1]
                # print(cur_idx)
                print(shortest, cur_ans_idx, cur_idx)

                if cur_idx == target_idx:
                    shortest = min(shortest, len(cur_ans_idx))
                    if len(cur_ans_idx) == shortest:
                        tmp = [wordList[i] for i in cur_ans_idx]
                        ret_list.append(tmp)
                if len(cur_ans_idx) >= shortest:
                    continue
                flag = True
                for j in range(len(wordList)):
                    if graph[cur_idx][j] and j not in cur_ans_idx:
                        flag = False
                        # queue.append((cur_ans_idx+[j]))
                        cur_ans_idx.append(j)
                        queue.append((cur_ans_idx.copy()))
                        cur_ans_idx.pop()
                        tmp_delete_list.append(j)
            # print("delete:", tmp_delete_list)
            for j in tmp_delete_list:
                for i in range(len(wordList)):
                    graph[i][j] = False
        # print(ret_list)
        return ret_list

    # version for refering the solution 
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     print("start")
    #     def diff_one(word1, word2):
    #         diff_cnt = 0
    #         for i in range(len(word1)):
    #             if word1[i] != word2[i]:
    #                 diff_cnt += 1
    #         return diff_cnt == 1
        
    #     if beginWord not in wordList:
    #         wordList.append(beginWord)
    #     if endWord not in wordList:
    #         return []

    #     graph = [[False]*len(wordList) for _ in range(len(wordList))]
    #     for i in range(len(wordList)):
    #         for j in range(len(wordList)):
    #             graph[i][j] = diff_one(wordList[i], wordList[j])

    #     begin_idx, target_idx = wordList.index(beginWord), wordList.index(endWord)
    #     queue = deque([begin_idx])
    #     trimed_graph = {begin_idx:[]}
    #     ret_list = []
    #     while queue:
    #         tmp_delete_set = set()
    #         print("len(queue):", len(queue))
    #         break_flag = False
    #         level = []
    #         print("len(level):", len(trimed_graph))
    #         for _ in range(len(queue)):
    #             cur_ans_idx = queue.popleft()
    #             cur_idx = cur_ans_idx
    #             # print(cur_idx)
    #             # print(len(level), cur_ans_idx, cur_idx)

    #             if cur_idx == target_idx or len(trimed_graph) > len(wordList):
    #                 break_flag = True

    #             if cur_idx not in trimed_graph:
    #                 trimed_graph[cur_idx] = []

    #             for j in range(len(wordList)):
    #                 if graph[cur_idx][j]:
    #                     # queue.append((cur_ans_idx+[j]))
    #                     if j not in trimed_graph:
    #                         trimed_graph[cur_idx] = j
    #                         queue.append(j)
    #                         tmp_delete_set.add(j)
    #                     else:
    #                         trimed_graph[cur_idx].append(j)

    #         print("delete:", len(tmp_delete_set))
    #         for j in tmp_delete_set:
    #             for i in range(len(wordList)):
    #                 graph[i][j] = False
    #         if break_flag:
    #             break
    #     # print(ret_list)
    #     return ret_list

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        print("start")
        def diff_one(word1, word2):
            diff_cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_cnt += 1
            return diff_cnt == 1
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return []

        graph = [[False]*len(wordList) for _ in range(len(wordList))]
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                graph[i][j] = diff_one(wordList[i], wordList[j])
        start_idx, target_idx = wordList.index(beginWord), wordList.index(endWord)
        # for i in range(len(wordList)):
        #     graph[i][start_idx] = False


        from copy import deepcopy
        graph_bak = deepcopy(graph)

        queue = deque([start_idx])
        level_list = []
        while queue:
            tmp_delete_set = set()
            print("len(queue):", len(queue))
            break_flag = False
            level = []
            print("len(level):", len(level_list))
            for _ in range(len(queue)):
                cur_ans_idx = queue.popleft()
                cur_idx = cur_ans_idx
                # print(cur_idx)
                # print(len(level), cur_ans_idx, cur_idx)

                if cur_idx == target_idx:
                    break_flag = True

                flag = True
                for j in range(len(wordList)):
                    if graph[cur_idx][j]:
                        flag = False
                        # queue.append((cur_ans_idx+[j]))
                        if j not in tmp_delete_set:
                            queue.append(j)
                            level.append(j)
                        tmp_delete_set.add(j)
                if flag:
                    for i in range(len(wordList)):
                        graph[i][cur_idx] = False
            if break_flag:
                break
            level_list.append(level)
            # print("delete:", len(tmp_delete_set))
            for j in tmp_delete_set:
                for i in range(len(wordList)):
                    graph[i][j] = False
        # print(ret_list)
        print("level_list", level_list)

        ret_list = []
        glb = 0
        # def dfs(idx, words):
        #     # print("words", words)
        #     nonlocal glb
        #     print(glb)
        #     glb += 1
        #     if len(words) == len(level_list)+1:
        #         if words[-1] == target_idx:
        #             ret_list.append([wordList[i] for i in words])
        #         return
        #     for nxt_word in level_list[len(words)-1][::-1]:
        #         # print("nxt", nxt_word)
        #         if graph_bak[idx][nxt_word]:
        #             words.append(nxt_word)
        #             dfs(nxt_word, words)
        #             words.pop()

        # dfs(start_idx, [start_idx])
        # print("ret_list", ret_list)

        level_list.insert(0, [start_idx])
        level_list.pop()
        print(level_list)
        def dfs(idx, words):
            print("words", words)
            nonlocal glb
            # print(glb)
            glb += 1
            if len(words) == len(level_list)+1:
                print("hay", words[-1], start_idx)
                if words[-1] == start_idx:
                    print("why")
                    ret_list.append([wordList[i] for i in words[::-1]])
                return
            for nxt_word in level_list[-1-(len(words)-1)]:
                print("nxt", nxt_word)
                if graph_bak[idx][nxt_word]:
                    words.append(nxt_word)
                    dfs(nxt_word, words)
                    words.pop()

        dfs(target_idx, [target_idx])
        print("ret_list", ret_list)

        return ret_list

# from collections import defaultdict
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         # "word masked one char ==> word" dict
#         prefix_mask = defaultdict(list)
#         for word in wordList:
#             for i in range(len(word)):
#                 prefix_mask[word[:i]+"*"+word[i+1:]].append(word)
        
#         graph = {beginWord: []}
#         q = deque([beginWord])
#         temp_q = deque()
#         go_on = True

#         # bfs builds the backtracking graph
#         while q and go_on:  
#             growinggraph = defaultdict(list)
#             levelsize = len(q)
#             for _ in range(levelsize):
                
#                 word = q.popleft()# pop the current word on the path 
                
#                 for i in range(len(word)):
#                     # call the candidate based on the masked dict
#                     for candidate in prefix_mask[word[:i] + "*" + word[i+1:]]:
#                         if candidate == endWord:
#                             # the candidate shows the end of building walking graph
#                             go_on = False
#                         if candidate not in graph:
#                             # growing
#                             if candidate not in growinggraph:
#                                 growinggraph[candidate] = [word]
#                                 q.append(candidate)
#                             else:
#                                 growinggraph[candidate].append(word)
#             # adding the added part
#             graph.update(growinggraph)
        
#         ret = []
        
#         print("graph", graph)
#         # DFS to restore the paths
#         glb = 0
#         def dfs(path, word):
#             nonlocal glb
#             print(glb)
#             glb += 1
#             path = path + [word]    
#             if graph[word] == []:
#                 # get to the beginword which cannot backtack anymore
#                 ret.append(list(path[::-1]))
#                 return
#             for nextword in graph[word]:
#                 dfs(path, nextword)
                
                
#         if endWord in graph:
#             dfs([], endWord)
#         else:
#             return []
        
#         return ret

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def diff_one(word1, word2):
            diff_cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_cnt += 1
            return diff_cnt == 1
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return []

        graph = [[False]*len(wordList) for _ in range(len(wordList))]
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                graph[i][j] = diff_one(wordList[i], wordList[j])
        start_idx, target_idx = wordList.index(beginWord), wordList.index(endWord)

        from copy import deepcopy
        graph_bak = deepcopy(graph)

        queue = deque([start_idx])
        level_list = [[start_idx]]
        while queue:
            tmp_delete_set = set()
            break_flag = False
            level = []
            for _ in range(len(queue)):
                cur_idx = queue.popleft()
                if cur_idx == target_idx:
                    break_flag = True
                flag = True
                for j in range(len(wordList)):
                    if graph[cur_idx][j]:
                        flag = False
                        if j not in tmp_delete_set:
                            queue.append(j)
                            level.append(j)
                        tmp_delete_set.add(j)
                if flag:
                    for i in range(len(wordList)):
                        graph[i][cur_idx] = False
            if break_flag:
                break
            level_list.append(level)
            for j in tmp_delete_set:
                for i in range(len(wordList)):
                    graph[i][j] = False
        ret_list = []
        level_list.pop()

        def dfs(idx, words):
            if len(words) == len(level_list)+1:
                if words[-1] == start_idx:
                    ret_list.append([wordList[i] for i in words[::-1]])
                return
            for nxt_word in level_list[-1-(len(words)-1)]:
                if graph_bak[nxt_word][idx]:
                    words.append(nxt_word)
                    dfs(nxt_word, words)
                    words.pop()

        dfs(target_idx, [target_idx])

        return ret_list


su = Solution()
# case MLE
beginWord = "cet"
endWord = "ism"
wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim"]
res = su.findLadders(beginWord, endWord, wordList)
# exit(0)

# case TLE
beginWord = "aaaaa"
endWord = "ggggg"
wordList = ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"]
res = su.findLadders(beginWord, endWord, wordList)
# exit(0)

# case std1
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
res = su.findLadders(beginWord, endWord, wordList)
ans = [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
#      6,0,1,2,5         6,0,3,4,5
assert(res == ans)
# exit(0)
# case std2
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
res = su.findLadders(beginWord, endWord, wordList)
ans = []
assert(res == ans)

# case boundry
beginWord = "hit"
endWord = "hig"
wordList = ["hia","hig"]
res = su.findLadders(beginWord, endWord, wordList)
ans = [["hit", "hig"]]
assert(res == ans)

# case boundry exist but cant reach
beginWord = "hit"
endWord = "hac"
wordList = ["hia","hac"]
res = su.findLadders(beginWord, endWord, wordList)
ans = []
assert(res == ans)

# case boundry 1 wordList
beginWord = "hit"
endWord = "hit"
wordList = ["hit"]
res = su.findLadders(beginWord, endWord, wordList)
ans = [["hit"]]
assert(res == ans)

# case boundry exist but cant reach
beginWord = "hit"
endWord = "hac"
wordList = ["hac"]
res = su.findLadders(beginWord, endWord, wordList)
ans = []
assert(res == ans)

