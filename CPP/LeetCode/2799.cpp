#include<iostream>
#include<vector>
#include<cassert>
#include<set>
#include<algorithm>
#include<unordered_map>
#include<string>
#include<sstream>

using namespace std;


class Solution1 {
    public:
        int countCompleteSubarrays(vector<int>& nums) {
            set<int> wholeDistinct, subDistinct;
            for(int i:nums){
                wholeDistinct.insert(i);
            }
            int target_size = wholeDistinct.size();
            int left=0, right=0;
            int ret=0;
            while(right<nums.size()){
                if(subDistinct.size() == target_size){
                    subDistinct.erase(nums[left]);
                    ret += left + 1;
                    left += 1;
                }else{
                    subDistinct.insert(nums[right]);
                    right += 1;
                }
            }
            return ret;
        }
    };

class Solution {
    public:
        int countCompleteSubarrays(vector<int>& nums) {
            set<int> wholeDistinct;
            unordered_map<int, int> subDistinct;
            for(int i:nums){
                wholeDistinct.insert(i);
            }
            int target_size = wholeDistinct.size();
            int left=0, right=0;
            int ret=0;
            bool flag=false;
            while(right<nums.size()){
                subDistinct[nums[right]] += 1;
                while(left<nums.size() && subDistinct.size() == target_size){
                    flag = true;
                    cout << "left" << left << endl;
                    if(!--subDistinct[nums[left]]){
                        subDistinct.erase(nums[left]);
                    }
                    left++;
                    ret += nums.size() - right;
                }
                cout << "tmp_ret" << ret << endl;
                right += 1;

            }
            cout << "ret" << ret << endl;
            return ret;
        }
    };


int main(void){
    Solution su;
    vector<int> nums;
    int res, ans;
    // case std1
    nums = {1,3,1,2,2};
    res = su.countCompleteSubarrays(nums);
    ans = 4;
    assert(res == ans);
    // case std2
    nums = {5,5,5,5};
    res = su.countCompleteSubarrays(nums);
    ans = 10;
    assert(res == ans); 
}
                        
