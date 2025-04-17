#include<vector>
#include<iostream>
#include<cassert>
#include<unordered_map>

using namespace std;
class Solution {
    public:
        long long countGood0(vector<int>& nums, int k) {
            /*
            至少有k对arr[i] == arr[j]，i<j意味着不重复
            暴力解法遍历所有的(i,j)，并统计其中相同的pair O(n^3)
            如果在遍历子数组(i,j)过程中，维护一个dict，可降低至O(n^2)
            对于每一个子数组，统计有多少重复字符，重复字符再计算组合数。

            如果能够知道所有子数组内重复字符数量，可以快速计算
            */

            // cout << "debug begin" << endl;
            // cout << isGood(nums, 0, nums.size(), k) << endl;
            // cout << "debug finish" << endl;
            long long ret=0;
            for(int i=0;i<nums.size();i++){
                int l=i, r=nums.size()-1, mid, find=0;
                while(l<=r){
                    mid = l+(r-l)/2;
                    if(isGood(nums, i, mid, k)){
                        find = mid;
                        r = mid-1;
                    }else{
                        l = mid+1;
                    }
                }
                if(find != 0)
                    ret += nums.size()-find;
                // cout << "ret" <<  ret << "find" << find << endl;
            }
            return ret;
        }

        bool isGood(vector<int>& nums, int l, int r, int k){
            unordered_map<int, int> seen;
            for(int i=l;i<=r;i++){
                if(seen.find(nums[i]) == seen.end()){
                    seen[nums[i]] = 1;
                }else{
                    seen[nums[i]] += 1;
                }
            }
            int cnt=0;
            for(auto [k,v]:seen){
                if(v>=2){
                    cnt += v*(v-1)/2;
                }
            }
            return cnt >= k;
        }
        long long countGood1(vector<int>& nums, int k) {
            int res=0;
            int l=0, r=0;
            unordered_map<int, int> d;
            for(r=0;r<nums.size();r++){
                k -= d[nums[r]]++;
                while(k <= 0)
                    k += --d[nums[l++]];
                res+=l;
            }
            return res;
        }

        long long countGood2(vector<int>& nums, int k) {
            cout << "debug begin" << endl;
            long long res=0;
            int l=0, r=0;
            unordered_map<int, int> d;
            for(r=0;r<nums.size();r++){
                d[nums[r]] +=1;
                if(d[nums[r]] >= 2){
                    k -= (d[nums[r]]-1);
                }

                while(k <= 0)
                    k += --d[nums[l++]];
                res+=l;
                cout << "l " << l << " r " << r << " res " << res << endl;
            }
            return res;
        }

        long long countGood(vector<int>& nums, int k) {
            cout << "debug begin" << endl;
            long long res=0;
            int l=0, r=0;
            unordered_map<int, int> d;
            for(r=0;r<nums.size();r++){
                d[nums[r]] +=1;
                if(d[nums[r]] >= 2){
                    k -= (d[nums[r]]-1);
                }

                if(k <= 0){
                    k += --d[nums[l++]];
                    res+=nums.size()-r;
                }
                cout << "l " << l << " r " << r << " res " << res << endl;
            }
            return res;
        }
    };

int main(void){
    Solution s;
    vector<int> nums;
    long long res, ans;
    int k;
    // case std1
    k = 10;
    nums = {1,1,1,1,1};
    res = s.countGood(nums, k);
    ans = 1;
    assert(res == ans);

    // case std2
    k = 2;
    nums = {3,1,4,3,2,2,4};
    res = s.countGood(nums, k);
    ans = 4;
    assert(res == ans);
}
                    
    
