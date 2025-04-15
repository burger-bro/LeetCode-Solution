#include<iostream>
#include<vector>
#include<cassert>
#include<set>
#include<algorithm>
#include<unordered_map>
using namespace std;


class Solution {
    public:
        bool divideArray(vector<int>& nums) {
            unordered_map<int, int> d;
            // for(auto n:nums){
            //     auto it = d.find(n);
            //     int tmp;
            //     if(it == d.end()){
            //         d.insert({n, 1});
            //     }else{
            //         d[n] += 1;
            //     }
            // }
            // 优化版写法：
            for(const auto& num:nums){
                d[num]++;
            }
            for(const auto& pair:d){
                if(pair.second%2!=0) return false;
            }
            return true;
        }
    };


int main(void){
    Solution s;
    vector<int> nums ;
    bool res, ans;
    // case std1
    nums  = {3,2,3,2,2,2};
    res = s.divideArray(nums );
    cout << "res: " << res << endl;
    ans = true;

}
            
