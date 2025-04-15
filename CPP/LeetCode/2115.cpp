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

class Solution {
    public:
        vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
            /*
            一个疑问：对于原料有依赖的，如2->3->1  3->2->1 
            对于第二种情况，存在第二轮再遇到还不满足的，因此不能用visited的flag来判断，
            只能用每次遍历完queue之后是否有减少的元素来判断；
            */
            set<string> suppliesSet(supplies.begin(), supplies.end());
            // for(auto r:suppliesSet){
            //     cout << r << endl;
            // }
            deque<int> unvisited;
            for(int i=0;i<recipes.size();i++){
                unvisited.push_back(i);
            }
            
            vector<string> ret;
            while(unvisited.size()!=0){
                int lastSize = unvisited.size();
                int cnt=0;
                while(cnt < lastSize){
                    int cur=unvisited.front();
                    unvisited.pop_front();
                    bool flag = true;
                    for(auto r:ingredients[cur]){
                        if(suppliesSet.find(r) == suppliesSet.end()){
                            flag = false;
                            break;
                        }
                    }
                    if(flag){
                        suppliesSet.insert(recipes[cur]);
                        ret.push_back(recipes[cur]);
                    }
                    else{
                        unvisited.push_back(cur);
                    }
                    cnt++;
                }
                if(lastSize == unvisited.size()) return ret;
            }
            return ret;
        }
    };


int main(void){
    Solution s;
    vector<string> recipes, supplies;
    vector<vector<string>> ingredients;
    vector<string> res, ans;
    // case std1
    recipes = {"bread"};
    ingredients = {{"yeast","flour"}};
    supplies = {"yeast","flour","corn"};
    res = s.findAllRecipes(recipes, ingredients, supplies);
    for(auto r:res){
        cout << r << endl;
    }
    ans = {"bread"};
    // assert(res == ans);
    // case std2
    recipes = {"bread","sandwich"};
    ingredients = {{"yeast","flour"},{"bread","meat"}};
    supplies = {"yeast","flour","meat"};
    res = s.findAllRecipes(recipes, ingredients, supplies);
    for(auto r:res){
        cout << r << endl;
    }
    ans = {"bread","sandwich"};
    assert(res == ans);
    // case std2
    recipes = {"bread","sandwich"};
    ingredients = {{"yeast","flour"},{"bread","meat"}};
    supplies = {"yeast","flour","meat"};
    res = s.findAllRecipes(recipes, ingredients, supplies);
    for(auto r:res){
        cout << r << endl;
    }
    ans = {"bread","sandwich"};
    assert(res == ans);
}
    
