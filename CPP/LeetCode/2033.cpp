
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

class Solution {
    public:
        int minOperations1(vector<vector<int>>& grid, int x) {
            /*
            grid[i][j] = t*x + mod，当所有的mod不相等时，无解
            现在求最小值：
            每一个grid[i][j]要被变为： (t+cnt)*x + mod，使得所有cnt之和最小
            什么情况下最小？猜测1：为均值时，但均值不能被整除时怎么办？
            */
            int m=grid.size(), n=grid[0].size();
            if(m==1 && n==1) return 0;
            int ref=grid[0][0]%x, sum=0, avg;
            int mid=0, mid_cnt=0;
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(grid[i][j]%x!=ref) return -1;
                    sum += grid[i][j];
                }
            }
            avg = sum/(m*n);
            cout << "ref:" << ref << endl;
            cout << "avg:" << avg << endl;
            avg = avg-ref;
            int tmp=avg/x;
            int tg1=x*tmp+ref, tg2=x*(tmp+1)+ref, tg3=x*(tmp-1)+ref;
            cout << "avgmod:" << avg << endl;
            cout << "tg:" << tg1 << " " << tg2 << endl;
            int cnt=0,cnt2=0,cnt3=0,cnt4=0;
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    cnt += abs(grid[i][j]-tg1)/x;
                    cnt2 += abs(grid[i][j]-tg2)/x;
                    cnt3 += abs(grid[i][j]-tg3)/x;
                }
            }
            // cout << cnt << " " << cnt2 << " " << cnt3 << " " << cnt4 << " " << endl;
            return min(min(cnt, cnt2), cnt3);
        }

        int minOperations(vector<vector<int>>& grid, int x) {
            /*
            grid[i][j] = t*x + mod，当所有的mod不相等时，无解
            现在求最小值：
            每一个grid[i][j]要被变为： (t+cnt)*x + mod，使得所有cnt之和最小
            什么情况下最小？猜测1：为均值时，但均值不能被整除时怎么办？
            */
            int m=grid.size(), n=grid[0].size();
            if(m==1 && n==1) return 0;
            int ref=grid[0][0]%x, sum=0, avg;
            vector<int> arr;
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(grid[i][j]%x!=ref) return -1;
                    sum += grid[i][j];
                    arr.push_back(grid[i][j]);
                }
            }
            sort(arr.begin(), arr.end());

            avg = arr[m*n/2];
            cout << "ref:" << ref << endl;
            cout << "avg:" << avg << endl;
            avg = avg-ref;
            int tmp=avg/x;
            int tg1=x*tmp+ref, tg2=x*(tmp+1)+ref, tg3=x*(tmp-1)+ref;
            cout << "avgmod:" << avg << endl;
            cout << "tg:" << tg1 << " " << tg2 << endl;
            int cnt=0,cnt2=0,cnt3=0,cnt4=0;
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    cnt += abs(grid[i][j]-tg1)/x;
                    cnt2 += abs(grid[i][j]-tg2)/x;
                    cnt3 += abs(grid[i][j]-tg3)/x;
                }
            }
            // cout << cnt << " " << cnt2 << " " << cnt3 << " " << cnt4 << " " << endl;
            return min(min(cnt, cnt2), cnt3);
        }
};

int main(void){
    Solution s;
    vector<vector<int>> edges;
    int n, res, ans;
    // case bug
    n = 92;
    edges = {{529,529,989},{989,529,345},{989,805,69}};
    res = s.minOperations(edges, n);
    cout << "res" << res << endl;
    ans = 25;
    assert(res == ans);
    // case std1
    n = 73;
    edges = {{931,128},{639,712}};
    res = s.minOperations(edges, n);
    cout << "res" << res << endl;
    ans = 12;
    assert(res == ans);
    // case std1
    n = 2;
    edges = {{2,4},{6,8}};
    res = s.minOperations(edges, n);
    cout << "res" << res << endl;
    ans = 4;
    assert(res == ans);
    // case std2
    n = 1;
    edges = {{1,5},{2,3}};
    res = s.minOperations(edges, n);
    cout << "res" << res << endl;
    ans = 5;
    assert(res == ans);
    // case std3
    n = 2;
    edges = {{1,2},{3,4}};
    res = s.minOperations(edges, n);
    cout << "res" << res << endl;
    ans = -1;
    assert(res == ans);
}
                
    