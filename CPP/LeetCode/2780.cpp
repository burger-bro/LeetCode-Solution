
#include<iostream>
#include<vector>
#include<cassert>
#include<set>
#include<algorithm>
#include<unordered_map>
#include<string>
#include<sstream>
#include<deque>
#include<cmath>
#include <cstdio>

using namespace std;

class Solution1 {
    public:
        int minimumIndex(vector<int>& nums) {
            // cout << getMode(nums, 0, 0) << endl;
            if(nums.size()==1) return -1;
            int left=0, right=nums.size()-1, mid;
            int leftMode, rightMode;
            int ret=-1;
            while(left<=right){
                mid = left+(right-left)/2;
                leftMode = getMode(nums, 0, mid);
                rightMode = getMode(nums, mid+1, nums.size()-1);
                cout <<"mid" << mid << endl;
                cout << leftMode << endl;
                cout << rightMode << endl;
                if(leftMode == rightMode && leftMode != -1){
                    ret = mid;
                    right = mid-1;
                }else{
                    left = mid+1;
                }
            }
            return ret;
        }
        int getMode(vector<int>& nums, int start, int end){  // inclusive ends
            int cnt=0, candi=-1;
            for(int i=start;i<end+1;i++){
                if(cnt==0){
                    candi = nums[i];
                    cnt++;
                    continue;
                }
                if(nums[i]==candi) cnt++;
                else cnt--;
            }
            return cnt==0?-1:candi;
        }
    };

class Solution {
    public:
        int minimumIndex1(vector<int>& nums) {
            // cout << getMode(nums, 0, 0) << endl;
            cout << "****************start****************" << endl;
            if(nums.size()==1) return -1;
            int left=0, right=nums.size()-1, mid;
            int leftMode, rightMode;
            int ret=-1;
            int ref=getMode(nums,0,nums.size()-1);
            while(left<=right){
                mid = left+(right-left)/2;
                leftMode = getMode(nums, 0, mid);
                rightMode = getMode(nums, mid+1, nums.size()-1);
                cout <<"mid" << mid << " ref" << ref << endl;
                cout << leftMode << endl;
                cout << rightMode << endl;
                if(leftMode == rightMode){
                    ret = mid;
                    right = mid-1;
                }else if(rightMode != ref){
                    right = mid-1;
                }
                else{
                    left = mid+1;
                }
            }
            return ret;
        }
        int getMode1(vector<int>& nums, int start, int end){  // inclusive ends
            int cnt=0, candi=-1;
            for(int i=start;i<end+1;i++){
                if(cnt==0){
                    candi = nums[i];
                    cnt++;
                    continue;
                }
                if(nums[i]==candi) cnt++;
                else cnt--;
            }
            return cnt==0?-1:candi;
        }
        int getMode(vector<int>& nums, int start, int end){  // inclusive ends
            int cnt=0, candi=-1;
            for(int i=start;i<end+1;i++){
                if(cnt==0) candi = nums[i];
                if(nums[i]==candi) cnt++;
                else cnt--;
            }
            return candi;
        }
        int minimumIndex(vector<int>& nums) {
            // cout << getMode(nums, 0, 0) << endl;
            cout << "****************start****************" << endl;
            int refCnt=0,curCnt=0;
            int ref=getMode(nums,0,nums.size()-1);
            for(int i=0;i<nums.size();i++){
                if(nums[i]==ref) refCnt++;
            }
            for(int i=0;i<nums.size();i++){
                if(nums[i]==ref) curCnt++;
                if(curCnt*2>(i+1) && (refCnt-curCnt)*2>(nums.size()-i-1)){
                    return i;
                }
            }
            return -1;
        }

        int minimumIndex2(vector<int>& nums) {
            // cout << getMode(nums, 0, 0) << endl;
            cout << "****************start****************" << endl;
            int cnt=0, candi=-1;
            int ref=getMode(nums,0,nums.size()-1);
            for(int i=0;i<nums.size();i++){
                if(cnt==0){
                    candi = nums[i];
                }
                if(nums[i]==candi) cnt++;
                else cnt--;

                if(cnt!=0 && candi==ref && getMode(nums,i,nums.size()-1)==ref){
                    return i-1;
                }
            }
            return -1;
        }
    };

int main(void){
    Solution s;
    vector<int> edges;
    int n, res, ans;
    // case bug2
    edges = {1,2,1,1};
    res = s.minimumIndex(edges);
    cout << "res" << res << endl;
    ans = 0;
    assert(res == ans);
    // case bug
    edges = {1,1,1,2};
    res = s.minimumIndex(edges);
    cout << "res" << res << endl;
    ans = 0;
    assert(res == ans);
    // case std1
    edges = {1,2,2,2};
    res = s.minimumIndex(edges);
    cout << "res" << res << endl;
    ans = 2;
    assert(res == ans);
    // case std2
    edges = {2,1,3,1,1,1,7,1,2,1};
    res = s.minimumIndex(edges);
    cout << "res" << res << endl;
    ans = 4;
    assert(res == ans);
    // case std3
    edges = {3,3,3,3,7,2,2};
    res = s.minimumIndex(edges);
    cout << "res" << res << endl;
    ans = -1;
    assert(res == ans);
    // case1
    edges = {1};
    res = s.minimumIndex(edges);
    cout << "res" << res << endl;
    ans = -1;
    assert(res == ans);
    // case2
    edges = {999,999};
    res = s.minimumIndex(edges);
    cout << "res" << res << endl;
    ans = 0;
    assert(res == ans);
}
                
        


