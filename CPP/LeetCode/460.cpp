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
    int counter=1;
};

class LFUCache {
    public:
        LFUCache(int capacity) {
            _capacity = capacity;
            head->next = tail;
            tail->prev = head;
        }
        
        int get(int key) {
            if(_dict.find(key) != _dict.end()){
                Node* pop = _dict[key];
                pop->counter++;
                if(pop->counter >= pop->prev->counter){
                    Node* insert = findInsert(pop);
                    popNode(pop);
                    addNode(pop, insert);
                }
                return _dict[key]->val;
            }else{
                return -1;
            }
        }
        
        void put(int key, int value) {

            Node* tmp=head;
            while(tmp->next!=nullptr){
                cout << "k" << tmp->key << " v" << tmp->val << " c" << tmp->counter << endl;
                tmp = tmp->next; 
            }

            if(_dict.find(key) == _dict.end()){
                if(_dict.size()==_capacity){
                    // delete the last one
                    Node* d = tail->prev;
                    popNode(d);
                    _dict.erase(d->key);
                    delete d;
                }
                Node* newN = new Node{key, value};
                Node* insert = findInsert(tail);
                addNode(newN, insert);
                _dict[key] = newN;
            }else{
                Node* pop = _dict[key];
                _dict[key]->val = value;
                pop->counter++;
                if(pop->counter >= pop->prev->counter){
                    Node* insert = findInsert(pop);
                    popNode(pop);
                    addNode(pop, insert);
                }
            }
        }

        Node* findInsert(Node* node){  //注意
            Node* p = node;
            while(p->counter <= node->counter){
                p = p->prev;
            }
            return p;
        }

        void popNode(Node* pop){
            Node* tmp_prv = pop->prev;
            pop->next->prev = pop->prev;
            tmp_prv->next = pop->next;
        }

        void addNode(Node* addN, Node* insert){  //注意
            Node* tmp_nxt = insert->next;
            insert->next = addN;
            addN->prev = insert;
            addN->next = tmp_nxt;
            tmp_nxt->prev = addN;
        }

        // void addNode(Node* addN){  //注意
        //     tail->prev->next = addN;
        //     addN->prev = tail->prev;
        //     addN->next = tail;
        //     tail->prev = addN;
        // }

    private:
        int _capacity=0;
        unordered_map<int, Node*> _dict;
        Node* head = new Node{-1, -1, nullptr, nullptr, INT_MAX};
        Node* tail = new Node{-1, -1, nullptr, nullptr, 1};
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
              
