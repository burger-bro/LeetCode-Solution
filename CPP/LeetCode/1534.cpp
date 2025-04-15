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
        int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
            int ret=0;
            for(int i=0;i<arr.size();i++){
                for(int j=i+1;j<arr.size();j++){
                    for(int k=j+1;k<arr.size();k++){
                        if(abs(arr[i]-arr[j]) <= a &&
                            abs(arr[j]-arr[k]) <= b &&
                            abs(arr[i]-arr[k]) <= c){
                                ret += 1;
                            }
                    }
                }
            }
            return ret;
        }
    };

int main(void){
    Solution s;
    vector<int> arr;
    int a, b, c, res, ans;
    // case std1
    arr = {3,0,1,1,9,7};
    a = 7, b = 2, c = 3;
    res = s.countGoodTriplets(arr, a, b, c);
    cout << "res: " << res << endl;
    ans = 4;
    // case std2
    arr = {1,1,2,2,3};
    a = 0, b = 0, c = 1;
    res = s.countGoodTriplets(arr, a, b, c);
    cout << "res: " << res << endl;
    ans = 0;
    assert(res == ans);
}
                
