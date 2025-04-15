#include<iostream>
#include<vector>
#include<cassert>
#include<set>
#include<algorithm>
using namespace std;

class Solution {
    public:
        long long repairCars(vector<int>& ranks, int cars) {
            // test
            // bool t1 = canRepair(199, ranks, cars);
            // cout << "test time: " << t1 << endl;
            long long mid, ret=0, left=0, right=(*max_element(ranks.begin(), ranks.end()))*cars*cars;
            // cout << "right:" << right << endl;
            while(left <= right){
                mid = left + (right-left)/2;
                if(this->canRepair(mid, ranks, cars)){
                    ret = mid;
                    right = mid-1;
                    cout << "mid:" << mid << endl;
                }else{
                    left = mid+1;
                }
            }
            // cout << "return:" << ret << endl;
            return ret;
        }

        bool canRepair(long long time, vector<int>& ranks, int cars){
            for(auto r:ranks){
                int maxCar=0, curTime=0;
                while(curTime <= time){ // binary_search
                    maxCar += 1;
                    curTime = r * maxCar * maxCar;
                }
                cars -= maxCar-1;
                if(cars <= 0) return true;
            }
            return false;
        }

    };

int main(void){
    Solution s;
    vector<int> rank;
    int cars, res, ans;
    // case bug
    rank = {1,1,3,3};
    cars = 74;
    res = s.repairCars(rank, cars);
    ans = 576;
    assert(res == ans);  
    // case std1
    rank = {4,2,3,1};
    cars = 10;
    res = s.repairCars(rank, cars);
    cout << "res: " << res << endl;
    ans = 16;
    // case std1
    rank = {5,1,8};
    cars = 6;
    res = s.repairCars(rank, cars);
    ans = 16;
    assert(res == ans);  
}
        
