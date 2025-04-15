#include<iostream>
#include<vector>
#include<cassert>
#include<set>
#include<algorithm>
#include<unordered_map>
#include<string>
#include<sstream>
#include<deque>

using namespace std;

class Solution {
    public:
        int countDays(int days, vector<vector<int>>& meetings) {
            sort(meetings.begin(), meetings.end()); //[](vector<int>a, vector<int> b){return a[0]<b[0];}
            for(auto m:meetings){
                cout << "{";
                cout << m[0] << " " << m[1];
                cout << "}" << endl;
            }
            int ret = 0;
            int end = 0;
            for(auto m:meetings){
                if(m[0]>end){
                    ret += m[0]-end-1;
                }
                end = max(end, m[1]);
                cout << "ret" << ret << endl;
            }
            cout << "end" << end << " days" << days << endl;
            if((days-end)>0) ret += (days-end);
            return ret;
        }
    };

int main(void){
    Solution s;
    vector<vector<int>> edges;
    int n, res, ans;
    // case std1
    n = 10;
    edges = {{5,7},{1,3},{9,10}};
    res = s.countDays(n, edges);
    cout << "res" << res << endl;
    ans = 2;
    assert(res == ans);
    // case std2
    n = 5;
    edges = {{2,4},{1,3}};
    res = s.countDays(n, edges);
    cout << "res" << res << endl;
    ans = 1;
    assert(res == ans);
    // case1
    n = 10;
    edges = {{4,5}};
    res = s.countDays(n, edges);
    cout << "res" << res << endl;
    ans = 8;
    assert(res == ans);
    // case2
    n = 10;
    edges = {{1,10}};
    res = s.countDays(n, edges);
    cout << "res" << res << endl;
    ans = 0;
    assert(res == ans);
}
        