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
        int longestNiceSubarray(vector<int>& nums) {
            // dfs中怎么完备地遍历所有子数组？
            // 这道题似乎应该使用滑动窗口
            int left=0, right=0;
            int longest=1;
            while(right < nums.size()){
                right++;
                for(int i=left;i<right;i++){
                    if((nums[i]&nums[right])!=0){
                        left = i+1;
                    }
                }
                longest = max(right-left+1, longest);
            }
            return longest;
        }
    };

int main(void){
    Solution s;
    vector<int> nums;
    int res, ans;
    // case bug
    nums = {536870399,890391654};
    res = s.longestNiceSubarray(nums);
    cout << "res: " << res << endl;
    ans = 1;
    assert(res == ans);
    // case std1
    nums = {1,3,8,48,10};
    res = s.longestNiceSubarray(nums);
    cout << "res: " << res << endl;
    ans = 3;
    assert(res == ans);
    // case std2
    nums = {3,1,5,11,13};
    res = s.longestNiceSubarray(nums);
    cout << "res: " << res << endl;
    ans = 1;
    assert(res == ans);
    // case bound1
    nums = {3};
    res = s.longestNiceSubarray(nums);
    cout << "res: " << res << endl;
    ans = 1;
    assert(res == ans);
    // case bound2
    nums = {3,8};
    res = s.longestNiceSubarray(nums);
    cout << "res: " << res << endl;
    ans = 2;
    assert(res == ans);
    // case perf1
    for(int i=1;i<10000;i++){
        nums.push_back(i);
    }
    res = s.longestNiceSubarray(nums);
    cout << "res: " << res << endl;
    ans = 1;
    assert(res == ans);
}
                    
