#include<iostream>
#include<vector>
#include<cassert>
#include<unordered_map>
using namespace std;

class Solution {
    public:
        int countPairs0(vector<int>& nums, int k) {
            int ret=0;
            for(int i=0;i<nums.size()-1;i++){
                for(int j=i+1;j<nums.size();j++){
                    if(nums[i]==nums[j] && (i*j)%k==0){
                        cout << i << " " << j << endl;
                        ret += 1;
                    }
                }
            }
            cout << "ret" << ret << endl;
            return ret;
        }

        int countPairs(vector<int>& nums, int k) {
            int ret=0;
            unordered_map<int, int> divisible, nondivisible;
            for(int i=0;i<nums.size();i++){
                if(i%k == 0){
                    divisible[nums[i]]++;
                }else{
                    nondivisible[nums[i]]++;
                }
            }
            for(auto [k,v]: divisible){
                ret += v*(v-1)/2;
                if(nondivisible.find(k) != divisible.end()){
                    ret += v*nondivisible[k];
                }
            }
            cout << "debug" << endl;
            for(auto [k,v]: divisible){
                cout << "k " << k << " v " << v << endl;
            }

            cout << "debug" << endl;
            for(auto [k,v]: nondivisible){
                cout << "k " << k << " v " << v << endl;
            }

            cout << "ret" << ret << endl;
            return ret;
        }
    };

int main(void){
    Solution s;
    vector<int> nums;
    int res, ans, k;
    // case bug
    nums = {10,2,3,4,9,6,3,10,3,6,3,9,1};
    k = 4;
    res = s.countPairs(nums, k);
    ans = 8;
    assert(res == ans);
    // case std1
    nums = {3,1,2,2,2,1,3};
    k = 2;
    res = s.countPairs(nums, k);
    ans = 4;
    assert(res == ans);
    // case std2
    nums = {1,2,3,4};
    k = 1;
    res = s.countPairs(nums, k);
    ans = 0;
    assert(res == ans);
}