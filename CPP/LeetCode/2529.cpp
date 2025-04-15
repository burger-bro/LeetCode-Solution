#include<vector>
#include<iostream>
#include<cassert>

using namespace std;

class Solution {
    public:
        int maximumCount0(vector<int>& nums) {
            int posNum=0, negNum=0;
            for(auto i:nums){
                if(i>0){
                    posNum++;
                }else if(i<0){
                    negNum++;
                }
            }
            return max(posNum, negNum);
        }

        int maximumCount(vector<int>& nums) {
            int mid, left=0, right=nums.size()-1;
            int neg=-1, pos=-1;
            while(left <= right){
                mid = (left+right)/2;
                // cout << mid << endl;
                if(nums[mid] > 0){
                    right = mid-1;
                    pos = mid;
                }else{
                    left = mid+1;
                }
            }
            left=0, right=nums.size()-1;
            while(left <= right){
                mid = (left+right)/2;
                if(nums[mid] < 0){
                    left = mid+1;
                    neg = mid;
                }else{
                    right = mid-1;
                }
            }
            cout << "pos" << pos << "neg" << neg << endl;
            pos = pos!=-1?nums.size()-pos:-1;
            neg = neg!=-1?neg+1:-1;
            return max(0, max(pos, neg));
        }
    };

int main(void){
    Solution s;
    vector<int> nums;
    int res, ans;
    // case std1
    nums = {-2,-1,-1,1,2,3};
    res = s.maximumCount(nums);
    ans = 3;
    assert(res == ans);
    // case std2
    nums = {-3,-2,-1,0,0,1,2};
    res = s.maximumCount(nums);
    ans = 3;
    assert(res == ans);
    // case std3
    nums = {5,20,66,1314};
    res = s.maximumCount(nums);
    ans = 4;
    assert(res == ans);
    // case1
    nums = {0,0,1,2};
    res = s.maximumCount(nums);
    ans = 2;
    assert(res == ans);
    // case2
    nums = {-3,-2,-1,0,0};
    res = s.maximumCount(nums);
    ans = 3;
    assert(res == ans);   
    // case3
    nums = {0,0,0,0};
    res = s.maximumCount(nums);
    ans = 0;
    assert(res == ans);   
    // case4
    nums = {-1};
    res = s.maximumCount(nums);
    ans = 1;
    assert(res == ans);   
}
