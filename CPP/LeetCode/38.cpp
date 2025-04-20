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
        string countAndSay(int n) {
            string start="1";
            while(--n){
                start = RLE(start);
            }
            return start;
        }

        string RLE(string a){
            string b;
            char last_ch='*';
            int cnt=0;
            for(int i=0;i<a.size();i++){
                if(last_ch!='*' && last_ch!=a[i]){
                    b += to_string(cnt)+last_ch;
                    cnt = 0;
                }
                last_ch = a[i];
                cnt++;
            }
            b += to_string(cnt)+last_ch;
            return b;
        }
    };


int main(void){
    Solution s;
    vector<int> nums;
    int n;
    string res, ans;
    // case bug
    n = 4;
    res = s.countAndSay(n);
    cout << "res: " << res << endl;
    ans = "1211";
    assert(res == ans);
    // case std1
    n = 1;
    res = s.countAndSay(n);
    cout << "res: " << res << endl;
    ans = "1";
    assert(res == ans);
}
                    
