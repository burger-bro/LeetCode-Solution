#include<iostream>
#include<vector>
#include<cassert>
#include<set>
#include<algorithm>
using namespace std;

class Solution {
    public:
        int maximumCandies(vector<int>& candies, long long k) {
            cout << "begin" << endl;
            int ret=0, mid, left=1, right=*max_element(candies.begin(), candies.end());
            cout << "debug" << right << endl;
            while(left <= right){
                mid = left + (right-left)/2;
                if(this->isValid(mid, candies, k)){
                    left = mid+1;
                    ret = mid;
                }else{
                    right = mid-1;
                }
            }
            cout << "ret: " << ret << endl;
            return ret;
        }
        bool isValid(int mid, vector<int>& candies, long long k){
            long long cnt=0;
            for(auto c: candies){
                cnt += c/mid;
                if(cnt>=k) return true;
            }
            return false;
        }
    };


    int main(void){
        Solution s;
        vector<int> candies;
        int k, res, ans;
        // case std1
        candies = {5,8,6};
        k = 3;
        res = s.maximumCandies(candies, k);
        cout << "res: " << res << endl;
        ans = 5;
        assert(res == ans);  
        // case std2
        candies = {2,5};
        k = 11;
        res = s.maximumCandies(candies, k);
        ans = 0;
        assert(res == ans);  
        // case1 全拆分
        candies = {11};
        k = 11;
        res = s.maximumCandies(candies, k);
        ans = 1;
        assert(res == ans);  
        // case1 多一个
        candies = {12};
        k = 11;
        res = s.maximumCandies(candies, k);
        ans = 1;
        assert(res == ans);  
        // case1 少一个
        candies = {11};
        k = 12;
        res = s.maximumCandies(candies, k);
        ans = 0;
        assert(res == ans);  
    }
        