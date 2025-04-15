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
        int maxArea(vector<int>& height) {
            int area=0;
            for(int i=0; i<height.size(); i++){
                if(height[i]==0) continue;
                for(int j=max(i,area/height[i]); j<height.size(); j++){
                    area = max(area,(j-i)*(min(height[i], height[j])));
                }
            }
            return area;
        }
    };


int main(void){
    Solution s;
    vector<int> nums;
    int res, ans;
    // case bug
    nums = {1,8,6,2,5,4,8,3,7};
    res = s.maxArea(nums);
    cout << "res: " << res << endl;
    ans = 49;
    assert(res == ans);
    // case std1
    nums = {1,1};
    res = s.maxArea(nums);
    cout << "res: " << res << endl;
    ans = 1;
    assert(res == ans);
    // case perf
    nums = {1,1};
    for(int i=5;i<10000;i++){
        nums.push_back(i);
    }
    res = s.maxArea(nums);
    cout << "res: " << res << endl;
    ans = 24995000;
    assert(res == ans);
}
                    
