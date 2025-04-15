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

struct Node{
    int key;
    int val;
    Node* prev;
    Node* next;
};

class LRUCache {
    public:
        LRUCache(int capacity) {
            _capacity = capacity;
            head->next = tail;
            tail->prev = head;
        }
        
        int get(int key) {
            if(_dict.find(key) != _dict.end()){
                Node* pop = _dict[key];
                popNode(pop);
                addNode(pop);

                return _dict[key]->val;
            }else{
                return -1;
            }
        }
        
        void put(int key, int value) {
            if(_dict.find(key) == _dict.end()){
                if(_dict.size()==_capacity){
                    // delete first one
                    Node* d = head->next;
                    popNode(d);
                    _dict.erase(d->key);
                    delete d;
                }
                Node* newN = new Node{key, value};
                addNode(newN);
                _dict[key] = newN;
            }else{
                Node* pop = _dict[key];
                popNode(pop);
                addNode(pop);
                _dict[key]->val = value;
            }
        }

        void popNode(Node* pop){
            Node* tmp_prv = pop->prev;
            pop->next->prev = pop->prev;
            tmp_prv->next = pop->next;
        }

        void addNode(Node* addN){
            tail->prev->next = addN;
            addN->prev = tail->prev;
            addN->next = tail;
            tail->prev = addN;
        }

    private:
        int _capacity=0;
        unordered_map<int, Node*> _dict;
        Node* head = new Node{-1, -1, nullptr, nullptr};
        Node* tail = new Node{-1, -1, nullptr, nullptr};
    };


int main(void){
    LRUCache c(3);
    // case std1
    // n = 7;
    // edges = {{1,2,3},{2,5,7},{3,5,1}};
    // queries = {5,6,2};
    // res = s.maxPoints(edges, queries);
    // ans = {5,8,1};
    // assert(res == ans);
}
              
