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
        int numberOfArrays0(vector<int>& differences, int lower, int upper) {
            if(differences.size()==0) return 0;
            int _min=0, _max=0, cur_sum=0;
            for(auto d: differences){
                cur_sum += d;
                _min = min(_min, cur_sum);
                _max = max(_max, cur_sum);
            }
            int x, u_bound;
            x = lower - _min;
            u_bound = x + _max;
            // int range=
            int ret = 0;
            cout << "debug l " <<  x << " u " << u_bound << endl;
            if(upper<u_bound){
                ret = 0;
            }else{
                ret = upper - u_bound + 1;
            }
            cout << "ret" << ret << endl;
            return ret;
        }

        int numberOfArrays(vector<int>& differences, int lower, int upper) {
            int _min=0, _max=0, cur_sum=0, cur_range=0, range=upper-lower;
            for(auto d: differences){
                cur_sum += d;
                _min = min(_min, cur_sum);
                _max = max(_max, cur_sum);
                cur_range = _max-_min;
                if(cur_range>range){
                    return 0;
                }
            }
            return range-cur_range+1;
        }

    };

int main(void){
    Solution s;
    vector<int> differences;
    int lower, upper;
    int res, ans;
    // case bug
    differences = {-40};
    lower = -46, upper = 53;
    res = s.numberOfArrays(differences, lower, upper);
    cout << "res: " << res << endl;
    ans = 60;
    assert(res == ans);
    // case std1
    differences = {1,-3,4};
    lower = 1, upper = 6;
    res = s.numberOfArrays(differences, lower, upper);
    cout << "res: " << res << endl;
    ans = 2;
    assert(res == ans);
    // case std2
    differences = {3,-4,5,1,-2};
    lower = -4, upper = 5;
    res = s.numberOfArrays(differences, lower, upper);
    cout << "res: " << res << endl;
    ans = 4;
    assert(res == ans);
    // case std3
    differences = {4,-7,2}; // x+4, x-3, x-1
    lower = 3, upper = 6;
    res = s.numberOfArrays(differences, lower, upper);
    cout << "res: " << res << endl;
    ans = 0;
    assert(res == ans);
}
                      
