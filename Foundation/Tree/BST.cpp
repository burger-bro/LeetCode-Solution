#include<iostream>
#include<queue>

using namespace std;

struct Node{
    int data;
    Node* parent;
    Node* left;
    Node* right;
};

class BST{
    private: Node* root;
    public:
    BST(void){root = nullptr;};
    bool insertVal(int val);
    bool insertValHelper(Node *&n, int val);
    bool deleteVal(int val);
    bool deleteValHelper(Node *&n, int val);
    bool deleteNode(Node *&n);
    void printTree();
    void inOrderTraversal(Node* n);
    void levelTraversal(Node* n);
    bool searchNode(int val);
    bool searchNodeHelper(Node*n, int val);
};

bool BST::insertVal(int val){
    return insertValHelper(root, val);
}

bool BST::insertValHelper(Node *&n, int val){
    if(n == nullptr){
        n = new Node{val};
        return true;
    }
    if(n->data == val){
        return false;
    }else if(n->data < val){
        insertValHelper(n->right, val);
    }else{
        insertValHelper(n->left, val);    
    }
    return true;
}

bool BST::deleteVal(int val){
    return deleteValHelper(root, val);
}

bool BST::deleteValHelper(Node *&n, int val){
    if(n == nullptr){return false;}
    if(val == n->data){
        return deleteNode(n);
    }else if(val > n->data){
        return deleteValHelper(n->right, val);
    }else{
        return deleteValHelper(n->left, val);
    }
}

bool BST::deleteNode(Node *&n){
    if(n->left == nullptr && n->right == nullptr){
        delete n;
        n = nullptr;
        return true;
    }
    Node *tmp, *maxValNode;
    if(n->right == nullptr){
        tmp = n->left;
        delete n;
        n = tmp;
    }else if(n->left == nullptr){
        tmp = n->right;
        delete n;
        n = tmp;
    }
    else{
        tmp = n;
        maxValNode = n->left;
        while(maxValNode->right != nullptr){
            tmp = maxValNode;
            maxValNode = maxValNode->right;
        }
        n->data = maxValNode->data;
        // delete maxValNode;
        // if(tmp == n){
        //     tmp->left = nullptr;  //未考虑该节点还有左子树的情况
        // }else{
        //     tmp->right = nullptr;
        // }
        if(tmp == n){
            tmp->left = maxValNode->left;
        }else{
            tmp->right = maxValNode->left;;
        }
        delete maxValNode;
    }

    return true;
}

void BST::printTree(void){
    cout << "print" << endl;
    // inOrderTraversal(root);
    levelTraversal(root);
    cout << endl;
}

void BST::inOrderTraversal(Node *n){
    if(n == nullptr) return;
    inOrderTraversal(n->left);
    cout << n->data << " ";
    inOrderTraversal(n->right);
}

void BST::levelTraversal(Node* n){
    queue<Node*> q;
    q.emplace(n);
    while(q.size() != 0){
        int ssize = q.size();
        for(int i=0;i<ssize;i++){
            Node* node=q.front();
            cout << node->data << " ";
            node->left && q.emplace(node->left);
            node->right && q.emplace(node->right);
            q.pop();
        }
        cout << endl;
    }
}

bool BST::searchNode(int val){
    return searchNodeHelper(root, val);
}

bool BST::searchNodeHelper(Node *n, int val){
    if(n == nullptr) return false;
    if(val == n->data){
        return true;
    }else if(val > n->data){
        return searchNodeHelper(n->right, val);
    }else{
        return searchNodeHelper(n->left, val);
    }
}

int main(void){
    cout << "begin" << endl;
    BST T;
    // int arr[] = {9, 12, 5, 3, 4, 1, 38};
    // T.insertVal(2);
    // T.insertVal(3);
    // T.insertVal(5);

    int arr[] = {50,25,10,5,2,9};
    for(auto i:arr){
        T.insertVal(i);
    }
    T.printTree();
    T.deleteVal(5);
    T.printTree();

    // int arr[] = {50,25,10,5,2,9};
    // for(auto i:arr){
    //     T.insertVal(i);
    // }
    // T.printTree();
    // T.deleteVal(5);
    // T.printTree();

    // cout << "search" << T.searchNode(99) << endl;
    // cout << "search" << T.searchNode(2) << endl;
    // cout << "search" << T.searchNode(9) << endl;
    // cout << "search" << T.searchNode(-200) << endl;
    
    cout << "end" << endl;
}
