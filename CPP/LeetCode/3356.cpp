#include<iostream>
#include<vector>
#include<cassert>
#include<set>

using namespace std;

class Solution {
    public:
        int minZeroArray0(vector<int>& nums, vector<vector<int>>& queries) {
            vector<int> tmp(nums);
            // vector<bool> sufficient(nums.size());
            set<int> sufficient, deal;
            int res;
            for(int i=0;i<nums.size();i++){
                // cout << "s" << i << endl;
                if(nums[i] != 0){
                    sufficient.insert(i);
                }
            }
            if(sufficient.empty()) return 0;
            // for(auto i:sufficient){
            //     cout << "s" << i << endl;
            // }

            for(int j=0;j<queries.size();j++){
                // cout << "hi" <<query[0] << query[1] << query[2] << endl;
                for(int i=queries[j][0];i<=queries[j][1];i++){
                    if(sufficient.find(i) != sufficient.end())
                        tmp[i] -= queries[j][2];
                    if(tmp[i] <= 0) sufficient.erase(i);
                    // if(tmp[i]<0) deal.insert(i);
                    if(sufficient.empty()) return j+1;
                }
            }
            // for (auto s: sufficient){
            //     cout << "sss" << s << endl;
            // }
            if(!sufficient.empty()) return -1;
            // 进阶题目
            // for(auto d: deal){
            //     // min_k(deal, )
            // }
            return res;
        }


        int minZeroArray1(vector<int>& nums, vector<vector<int>>& queries) {
            vector<int> tmp(nums);
            set<int> sufficient, deal;
            int res;
            for(int i=0;i<nums.size();i++){
                if(nums[i] != 0){
                    sufficient.insert(i);
                }
            }
            if(sufficient.empty()) return 0;
            for(int j=0;j<queries.size();j++){
                for(int i=queries[j][0];i<=queries[j][1];i++){
                    if(sufficient.find(i) != sufficient.end())
                        tmp[i] -= queries[j][2];
                    if(tmp[i] <= 0) sufficient.erase(i);
                    if(sufficient.empty()) return j+1;
                }
            }
            if(!sufficient.empty()) return -1;
            return res;
        }

        int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
            int ret=-1, mid, left=0, right=queries.size()-1;
            bool flag=true;
            for(auto n: nums){
                if(n!=0) flag=false;
            }
            if(flag) return 0;
            while(left <= right){
                mid = (left+right)/2;
                if(this->isValid(mid, nums, queries)){
                    ret = mid;
                    right = mid-1;
                }
                else
                    left = mid+1;
            }
            return ret==-1?-1:ret+1;
        }
        bool isValid(int k, vector<int>& nums, vector<vector<int>>& queries){
            vector<int> diff(nums.size()+1);
            for(int i=0;i<=k;i++){
                diff[queries[i][0]] += queries[i][2];
                diff[queries[i][1]+1] -= queries[i][2];
            }
            int total=0;
            for(int i=0;i<nums.size();i++){
                total += diff[i];
                if(total<nums[i]) return false;
            }
            return true;
        }
    };


int main(void){
    Solution s;
    vector<int> nums;
    vector<vector<int>> queries;
    int res, ans;
    // case std1
    nums = {2,0,2};
    queries = {{0,2,1},{0,2,1},{1,1,3}};
    res = s.minZeroArray(nums, queries);
    cout << "res: " << res << endl;
    ans = 2;
    assert(res == ans);  
    // case std2
    nums = {4,3,2,1};
    queries = {{1,3,2},{0,2,1}};
    res = s.minZeroArray(nums, queries);
    ans = -1;
    assert(res == ans);  
}
    