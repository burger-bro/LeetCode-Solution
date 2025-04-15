#include<iostream>
#include<vector>
#include<cassert>
#include<set>
#include<algorithm>
#include<unordered_map>
#include<string>
#include<sstream>

using namespace std;
class Solution {
    public:
        int isPrefixOfWord0(string sentence, string searchWord) {
            vector<string> tokens;
            this->split(sentence, tokens, " ");
            // for(auto t:tokens){
            //     cout << "t:" << t << endl;
            // }
            for(int i=0;i<tokens.size();i++){
                // if(this->startWith(tokens[i], searchWord)) return i+1;
                if(searchWord == tokens[i].substr(0, searchWord.size())){
                    return i+1;
                }
            }
            return -1;
        }

        void split(const std::string& s, std::vector<std::string>& tokens, const std::string& delimiters = " ") {
            std::string::size_type lastPos = s.find_first_not_of(delimiters, 0);
            std::string::size_type pos = s.find_first_of(delimiters, lastPos);
            while (std::string::npos != pos || std::string::npos != lastPos) {
                tokens.push_back(s.substr(lastPos, pos - lastPos));
                lastPos = s.find_first_not_of(delimiters, pos);
                pos = s.find_first_of(delimiters, lastPos);
            }
        }

        bool startWith(const std::string& s1, const std::string& s2){
            if(s1.size()<s2.size()) return false;
            int minLength = s2.size();
            for(int i=0;i<minLength;i++){
                if(s1[i] != s2[i]) return false;
            }
            return true;
        }

        int isPrefixOfWord(string sentence, string searchWord) {
            stringstream ss(sentence);
            string word;
            int cnt=1;
            while(getline(ss, word, ' ')){
                if(searchWord == word.substr(0, searchWord.size())) return cnt;
                cnt++;
            }
            return -1;
        }
    };

int main(void){
    Solution s;
    string sentence, searchWord;
    int res, ans;
    // case std1
    sentence = "i love eating burger";
    searchWord = "burg";
    res = s.isPrefixOfWord(sentence, searchWord);
    cout << "res: " << res << endl;
    ans = 4;
    assert(res == ans);
}
                
