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
        int countCompleteComponents(int n, vector<vector<int>>& edges) {
            vector<int> arr(n);
            for(int i=0;i<arr.size();i++){
                arr[i] = i;
            }
            for(auto e: edges){
                arr[e[0]] = e[0];
                arr[e[1]] = e[1];
            }
            for(auto e:edges){
                merge(e[0], e[1], arr);
            }
            unordered_map<int, unordered_map<int, int>> components;
            for(int i=0;i<arr.size();i++){
                if(i==arr[i]){
                    unordered_map<int, int> tmp;
                    tmp[i] = 0;
                    components[i] = tmp;
                }
            }
            for(auto e:edges){
                components[find(e[0], arr)][e[0]] += 1;
                components[find(e[1], arr)][e[1]] += 1;
            }
            int ret = 0;
            for(auto [k,v]:components){
                // cout << k << v.size() << endl;
                bool flag = true;
                for(auto [kk,vv]: v){
                    // cout << "vv" << vv << endl;
                    if(vv != v.size()-1){
                        flag = false;
                        break;
                    }
                }
                ret += flag?1:0;
            }
            return ret;
        }
        int find(int i, vector<int>& arr){
            return (arr[i] == i)?i:find(arr[i], arr);
        }
        void merge(int i, int j, vector<int>& arr){
            arr[find(j, arr)] = arr[(find(i, arr))];
        }
    };

class Solution {
    public:
        int countCompleteComponents(int n, vector<vector<int>>& edges) {
            vector<int> arr(n);
            for(int i=0;i<arr.size();i++){
                arr[i] = i;
            }
            for(auto e:edges){
                merge(e[0], e[1], arr);
            }
            unordered_map<int, unordered_map<int, int>> components;
            for(int i=0;i<arr.size();i++){
                if(i==arr[i]){
                    unordered_map<int, int> tmp;
                    tmp[i] = 0;
                    components[i] = tmp;
                }
            }
            for(auto e:edges){
                components[find(e[0], arr)][e[0]] += 1;
                components[find(e[1], arr)][e[1]] += 1;
            }
            int ret = 0;
            for(auto [k,v]:components){
                bool flag = true;
                for(auto [kk,vv]: v){
                    if(vv != v.size()-1){
                        flag = false;
                        break;
                    }
                }
                ret += flag?1:0;
            }
            return ret;
        }
        int find(int i, vector<int>& arr){
            return (arr[i] == i)?i:this->find(arr[i], arr);
        }
        void merge(int i, int j, vector<int>& arr){
            arr[this->find(j, arr)] = arr[(this->find(i, arr))];
        }
    };


int main(void){
    Solution s;
    vector<vector<int>> edges;
    int n, res, ans;
    // case std1
    n = 6;
    edges = {{0,1},{0,2},{1,2},{3,4}};
    res = s.countCompleteComponents(n, edges);
    cout << "res" << res << endl;
    ans = 3;
    assert(res == ans);
    // case std2
    n = 6;
    edges = {{0,1},{0,2},{1,2},{3,4},{3,5}};
    res = s.countCompleteComponents(n, edges);
    cout << "res" << res << endl;
    ans = 1;
    assert(res == ans);
}
        
