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
        long long countFairPairs(vector<int>& nums, int lower, int upper) {
            /*
            lower <= nums[i] + nums[j] <= upper
            l_d + nums[j] <=  nums[i] + nums[j] <= u_d + nums[j]
            */
            long long ans=0;
            sort(nums.begin(), nums.end());
            for(int left=0;left<nums.size();left++){
                int l=left+1, r=nums.size()-1;
                int mid, c_lower=-1, c_upper=-1;
                int target = lower - nums[left];
                while(l <= r){
                    mid = l + (r-l)/2;
                    if(nums[mid]>=target){
                        c_lower = mid;
                        r = mid-1;
                    }else{
                        l = mid+1;
                    }
                }
                target = upper - nums[left];
                l=left+1, r=nums.size()-1;
                while(l <= r){
                    mid = l + (r-l)/2;
                    if(nums[mid]<=target){
                        c_upper = mid;
                        l = mid+1;
                    }else{
                        r = mid-1;
                    }
                }
                // cout << "left:" << left << " c_lower:" << c_lower << " c_upper:" << c_upper << endl;
                if(c_lower != -1 && c_upper != -1 && c_lower <= c_lower){
                    ans += c_upper - c_lower + 1;
                }
            }
            cout << "ans" << ans << endl;
            return ans;
        }

        // int find(vector<int>& nums, int left, int right, int target){
        //     int mid, ret=-1;
        //     while(left <= right){
        //         if(nums[mid])
        //     }
        // }
    };


    
int main(void){
    Solution s;
    vector<int> nums;
    int n, lower, upper;
    long long res, ans;
    // case 1
    nums = {0,1,7,4,4,5};
    lower = 3;
    upper = 6;
    res = s.countFairPairs(nums, lower, upper);
    cout << "res: " << res << endl;
    ans = 6;
    assert(res == ans);
    // case 2
    nums = {1,7,9,2,5};
    lower = 11;
    upper = 11;
    res = s.countFairPairs(nums, lower, upper);
    cout << "res: " << res << endl;
    ans = 1;
    assert(res == ans);
}
                    
