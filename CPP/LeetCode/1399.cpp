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
        int countLargestGroup(int n) {
            vector<int> sums(37);
            for (int i = 1; i <= n; i++) sums[digsum(i)]++;
    
            int maxi = 0, count = 0;
            for (int i : sums) 
                if (i > maxi) maxi = i, count = 1;
                else if (i == maxi) ++count;
            
            return count;
        }
        int digsum(int n) {
            int sum = 0;
            while (n) {
                sum += n % 10;
                n /= 10;
            }
            return sum;
        }
    };


int main(void){
    Solution s;
    int n;
    int res, ans;
    // case std1
    n = 13;
    res = s.countLargestGroup(n);
    cout << "res: " << res << endl;
    ans = 4;
    assert(res == ans);
    // case std2
    n = 2;
    res = s.countLargestGroup(n);
    cout << "res: " << res << endl;
    ans = 2;
    assert(res == ans);
}
                        
