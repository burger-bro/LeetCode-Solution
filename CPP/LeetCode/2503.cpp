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
#include<cstdio>
#include<deque>
#include<queue>

using namespace std;

class Solution {
    public:
        vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
            vector<vector<int>> queiresIdx;
            for(int i=0;i<queries.size();i++){
                queiresIdx.push_back({queries[i], i});
            }
            sort(queiresIdx.begin(), queiresIdx.end(), [](auto& a, auto& b){return a[0]<b[0];});
            for(auto q: queiresIdx){
                cout << "q:" << q[0] << " idx:" << q[1] << endl;
            }
            deque<pair<int, int>> dq;
            dq.push_back(make_pair(0, 0));
            int curIdx=0, curPts=0;
            int m=grid.size(), n=grid[0].size();
            vector<vector<bool>> visited(m, vector<bool>(n, false));
            visited[0][0] = true;
            vector<int> ret(queries.size());
            cout << "mn" << m << "," << n << "queries" << queries.size() <<endl;
            vector<vector<int>> directions={{0,1},{0,-1},{1,0},{-1,0}};
            while(curIdx<queiresIdx.size() && dq.size()!=0){
                bool updated=false;
                for(int i=0;i<dq.size();i++){
                    pair<int, int>& xy = dq.front();
                    cout << "cur_pos" << xy.first << "," << xy.second << endl;
                    cout << "curIdx" << curIdx << endl;
                    if(grid[xy.first][xy.second]<queiresIdx[curIdx][0]){
                        curPts++;
                        updated = true;
                        for(auto dir:directions){
                            int newX=xy.first+dir[0], newY=xy.second+dir[1];
                            if((0<=newX)&&(newX<m)&&(0<=newY)&&(newY<n)&&!visited[newX][newY]){
                                dq.push_back(make_pair(newX, newY));
                                visited[newX][newY] = true;
                            }
                        }
                    }else{
                        dq.push_back(xy);
                    }
                    dq.pop_front();
                }
                if(!updated){
                    ret[queiresIdx[curIdx][1]] = curPts;
                    curIdx++;
                }
            }
            while(curIdx<queiresIdx.size()){
                ret[queiresIdx[curIdx][1]] = curPts;
                curIdx++;
            }
            // for(auto q: ret){
            //     cout << "ret:" << q;
            // }
            // cout << endl;
            return ret;
        }
    };

class Solution {
    public:
        vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
            vector<vector<int>> queiresIdx;
            for(int i=0;i<queries.size();i++){
                queiresIdx.push_back({queries[i], i});
            }
            sort(queiresIdx.begin(), queiresIdx.end(), [](auto& a, auto& b){return a[0]<b[0];});
            // deque<pair<int, int>> dq;
            // dq.push_back(make_pair(0, 0));
            auto cmp = [&grid](const auto& a, const auto& b) {
                return grid[a.first][a.second] > grid[b.first][b.second];
            };
            priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> dq(cmp);
            dq.push(make_pair(0, 0));

            int curIdx=0, curPts=0;
            int m=grid.size(), n=grid[0].size();
            vector<vector<bool>> visited(m, vector<bool>(n, false));
            visited[0][0] = true;
            vector<int> ret(queries.size());
            vector<vector<int>> directions={{0,1},{0,-1},{1,0},{-1,0}};
            while(curIdx<queiresIdx.size() && dq.size()!=0){
                bool updated=false;
                for(int i=0;i<dq.size();i++){
                    pair<int, int> xy = dq.top();
                    if(grid[xy.first][xy.second]>queiresIdx[curIdx][0]){
                        break;
                    }
                    dq.pop();
                    if(grid[xy.first][xy.second]<queiresIdx[curIdx][0]){
                        curPts++;
                        updated = true;
                        for(auto dir:directions){
                            int newX=xy.first+dir[0], newY=xy.second+dir[1];
                            if((0<=newX)&&(newX<m)&&(0<=newY)&&(newY<n)&&!visited[newX][newY]){
                                dq.push(make_pair(newX, newY));
                                visited[newX][newY] = true;
                            }
                        }
                    }else{
                        dq.push(xy);
                    }
                }
                if(!updated){
                    ret[queiresIdx[curIdx][1]] = curPts;
                    curIdx++;
                }
            }
            while(curIdx<queiresIdx.size()){
                ret[queiresIdx[curIdx][1]] = curPts;
                curIdx++;
            }
            return ret;
        }
    };

class Solution {
    public:
        vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
            vector<vector<int>> queiresIdx;
            for(int i=0;i<queries.size();i++){
                queiresIdx.push_back({queries[i], i});
            }
            sort(queiresIdx.begin(), queiresIdx.end(), [](auto& a, auto& b){return a[0]<b[0];});
            auto cmp = [&grid](const auto& a, const auto& b) {
                return grid[a.first][a.second] > grid[b.first][b.second];
            };
            priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> dq(cmp);
            dq.push(make_pair(0, 0));
            int curIdx=0, curPts=0;
            int m=grid.size(), n=grid[0].size();
            vector<vector<bool>> visited(m, vector<bool>(n, false));
            visited[0][0] = true;
            vector<int> ret(queries.size());
            vector<vector<int>> directions={{0,1},{0,-1},{1,0},{-1,0}};
            while(curIdx<queiresIdx.size() && dq.size()!=0){
                bool updated=false;
                for(int i=0;i<dq.size();i++){
                    pair<int, int> xy = dq.top();
                    if(grid[xy.first][xy.second]>=queiresIdx[curIdx][0]){
                        break;
                    }
                    dq.pop();
                    curPts++;
                    updated = true;
                    for(auto dir:directions){
                        int newX=xy.first+dir[0], newY=xy.second+dir[1];
                        if((0<=newX)&&(newX<m)&&(0<=newY)&&(newY<n)&&!visited[newX][newY]){
                            dq.push(make_pair(newX, newY));
                            visited[newX][newY] = true;
                        }
                    }
                }
                if(!updated){
                    ret[queiresIdx[curIdx][1]] = curPts;
                    curIdx++;
                }
            }
            while(curIdx<queiresIdx.size()){
                ret[queiresIdx[curIdx][1]] = curPts;
                curIdx++;
            }
            return ret;
        }
    };


int main(void){
    Solution s;
    vector<vector<int>> edges;
    vector<int> queries, ans, res;
    int n;
    // case bug
    n = 7;
    edges = {{249472,735471,144880,992181,760916,920551,898524,37043,422852,194509,714395,325171},{295872,922051,900801,634980,644237,912433,857189,98466,725226,984534,370121,399006},{618420,573065,587011,298153,694872,12760,880413,593508,474772,291113,852444,77998},{67650,426517,146447,190319,379151,184754,479219,106819,138473,865661,799297,228827},{390392,789371,772048,730506,7144,862164,650590,21524,879440,396198,408897,851020},{932044,662093,436861,246956,128943,167432,267483,148325,458128,418348,900594,831373},{742255,795191,598857,441846,243888,777685,313717,560586,257220,488025,846817,554722},{252507,621902,87704,599753,651175,305330,620166,631193,385405,183376,432598,706692},{984416,996917,586571,324595,784565,300514,101313,685863,703194,729430,732044,349877},{155629,290992,539879,173659,989930,373725,701670,992137,893024,455455,454886,559081},{252809,641084,632837,764260,68790,732601,349257,208701,613650,429049,983008,76324},{918085,126894,909148,194638,915416,225708,184408,462852,40392,964501,436864,785076},{875475,442333,111818,494972,486734,901577,46210,326422,603800,176902,315208,225178},{171174,458473,744971,872087,680060,95371,806370,322605,349331,736473,306720,556064},{207705,587869,129465,543368,840821,977451,399877,486877,327390,8865,605705,481076}};
    queries = {690474,796832,913701,939418,46696,266869,150594,948153,718874};
    res = s.maxPoints(edges, queries);
    ans = {5,8,1};
    assert(res == ans);
    // case std1
    n = 7;
    edges = {{1,2,3},{2,5,7},{3,5,1}};
    queries = {5,6,2};
    res = s.maxPoints(edges, queries);
    ans = {5,8,1};
    assert(res == ans);
    // case std2
    n = 2;
    edges = {{5,2,1},{1,1,2}};
    queries = {3};
    res = s.maxPoints(edges, queries);
    ans = {0};
    assert(res == ans);
}
                

