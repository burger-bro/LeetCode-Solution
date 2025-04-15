#include<iostream>
#include<vector>
#include<cassert>
#include<set>
#include<algorithm>
#include<unordered_map>
#include<string>
#include<sstream>
#include<deque>

using namespace std;


class Solution1 {
public:
    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        vector<vector<int>> axisX, axisY;
        for(auto r:rectangles){
            axisX.push_back({r[0], r[2]});
            axisY.push_back({r[1], r[3]});
        }
        bool Y = checkAxis(axisY), X = checkAxis(axisX);
        return X || Y;
    }
    bool checkAxis(vector<vector<int>>& axis){
        sort(axis.begin(), axis.end(), [](auto& a,auto& b){
            if(a[0]==b[0])
                return a[1]<b[1];
            return a[0]<b[0];
        });
        // for(auto r:axis){
        //     cout << r[0] << r[1] << endl;
        // }
        for(auto r:axis){
            cout << r[0] << r[1] << endl;
        }
        int pt1 = 0, pt2 = 1, border=-1; // 边界条件记得处理
        int cnt = 0;
        while(pt1 < axis.size() && pt2 < axis.size()){
            // if(axis[pt1][0]<border){
            //     pt1++;
            //     pt2++;
            // }
            if(axis[pt1][1] > axis[pt2][0]){
                pt1++;
                pt2 = pt1+1;
            }else if(axis[pt1][1] == axis[pt2][0]){
                pt2++; // 如果后面没有了，判断可能有问题
                if(pt2 >= axis.size()){
                    cnt++;
                    // return cnt==2;
                }
            }else if(axis[pt1][1] < axis[pt2][0]){
                // border = axis[pt1][1];
                pt1++;
                cnt++;
                pt2 = pt1+1;
            }
            cout << "pt1:" << pt1 << " pt2:" << pt2 << " cnt" << cnt << endl;
            if(cnt == 2){
                cout << "check true" << endl;
                return true;
            }
        }
        cout << "check false" << endl;
        return false;
    }
};

class Solution {
    public:
        bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
            vector<vector<int>> axisX, axisY;
            for(auto r:rectangles){
                axisX.push_back({r[0], r[2]});
                axisY.push_back({r[1], r[3]});
            }
            if(checkAxis(axisX)) return true;
            if(checkAxis(axisY)) return true;
            return false;
        }
        bool checkAxis(vector<vector<int>>& axis){
            sort(axis.begin(), axis.end(), [](auto& a,auto& b){
                if(a[0]==b[0])
                    return a[1]<b[1];
                return a[0]<b[0];
            });
            int pt1 = 0, pt2 = 1, border=axis[pt1][1]; // 边界条件记得处理
            int cnt = 0;
            while(pt1 < axis.size() && pt2 < axis.size()){
                if(border > axis[pt2][0]){
                    pt1++;
                    border = max(border, axis[pt1][1]);
                    pt2 = pt1+1;
                }else if(border == axis[pt2][0]){
                    pt2++; // 如果后面没有了，判断可能有问题
                    if(pt2 >= axis.size()){
                        cnt++;
                    }
                }else if(border < axis[pt2][0]){
                    pt1++;
                    border = axis[pt1][1];
                    cnt++;
                    pt2 = pt1+1;
                }
                cout << "pt1:" << pt1 << " pt2:" << pt2 << " cnt" << cnt << endl;
                if(cnt == 2){
                    cout << "check true" << endl;
                    return true;
                }
            }
            cout << "check false" << endl;
            return false;
        }
    };

int main(void){
    Solution s;
    vector<vector<int>> edges;
    int n;
    bool res, ans;
    // case std1
    n = 5;
    edges = {{1,0,5,2},{0,2,2,4},{3,2,5,3},{0,4,4,5}};
    res = s.checkValidCuts(n, edges);
    cout << "res" << res << endl;
    ans = true;
    assert(res == ans);
    // case std2
    n = 4;
    edges = {{0,0,1,1},{2,0,3,4},{0,2,2,3},{3,0,4,3}};
    res = s.checkValidCuts(n, edges);
    cout << "res" << res << endl;
    ans = true;
    assert(res == ans);

    // case std3
    n = 4;
    edges = {{0,2,2,4},{1,0,3,2},{2,2,3,4},{3,0,4,2},{3,2,4,4}};
    res = s.checkValidCuts(n, edges);
    cout << "res" << res << endl;
    ans = false;
    assert(res == ans);

    // case std21
    n = 4;
    edges = {{0,0,1,1},{2,0,3,4},{0,2,1,3},{3,0,4,3}};
    res = s.checkValidCuts(n, edges);
    cout << "res" << res << endl;
    ans = true;
    assert(res == ans);
    // case std22
    n = 4;
    edges = {{0,0,1,1},{2,0,3,4},{0,2,1,3}};
    res = s.checkValidCuts(n, edges);
    cout << "res" << res << endl;
    ans = false;
    assert(res == ans);
    // case bug
    n = 4;
    edges = {{0,0,1,4},{1,0,2,3},{2,0,3,3},{3,0,4,3},{1,3,4,4}};
    res = s.checkValidCuts(n, edges);
    cout << "res" << res << endl;
    ans = false;
    assert(res == ans);
}
        
