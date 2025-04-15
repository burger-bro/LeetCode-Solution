#include<iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

using namespace std;

class Solution {
    public:
        TreeNode* deleteNode(TreeNode* root, int key) {
            helper(root, key);
            return root;
        }

        bool helper(TreeNode*& n, int key){
            if(n == nullptr){return false;}
            if(key == n->val){
                delete_(n);    
            }else if(key > n->val){
                helper(n->right, key);
            }else{
                helper(n->left, key);
            }
            return true;
        }

        bool delete_(TreeNode*& n){
            if(n->left == nullptr && n->right == nullptr){
                delete n;
                n = nullptr;
                return true;
            }
            TreeNode *tmp, *maxValNode;
            if(n->right == nullptr){
                tmp = n->left;
                delete n;
                n = tmp;
            }else if(n->left == nullptr){
                tmp = n->right;
                delete n;
                n = tmp;
            }else{
                tmp = n;
                maxValNode = n->left;
                while(maxValNode->right != nullptr){
                    tmp = maxValNode;
                    maxValNode = maxValNode->right;
                }
                n->val = maxValNode->val;
                if(tmp == n){
                    tmp->left = maxValNode->left;
                }else{
                    tmp->right = maxValNode->left;
                }
                delete maxValNode;
            }
            return true;
        }
    };


int main(void){
    cout << "begin" << endl;
    Solution s;
    // int arr[] = {9, 12, 5, 3, 4, 1, 38};
    // T.insertVal(2);
    // T.insertVal(3);
    // T.insertVal(5);
    // cout << "search" << T.searchNode(99) << endl;
    // cout << "search" << T.searchNode(2) << endl;
    // cout << "search" << T.searchNode(9) << endl;
    // cout << "search" << T.searchNode(-200) << endl;
    
    cout << "end" << endl;
}
    
