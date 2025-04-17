#include<iostream>
#include<queue>

using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
    int height;
};

class AVL{
    private: Node* root;
    public:
    AVL(void){root = nullptr;};
    bool insertVal(int val);
    bool insertValHelper(Node *&n, int val);
    bool deleteVal(int val);
    bool deleteValHelper(Node *&n, int val);
    bool deleteNode(Node *&n);
    void printTree();
    void inOrderTraversal(Node* n);
    void levelTraversal(Node* n);
    bool searchNode(int val);
    bool searchNodeHelper(Node* n, int val);
    int getHeight(Node* n);
    int getFactor(Node* n);
    void rotateLeft(Node*& n);
    void rotateRight(Node*& n);
    void rebalance(Node*& n);
};

int AVL::getHeight(Node* n){
    if(n == nullptr){
        return -1;
    }else{
        return max(getHeight(n->left), getHeight(n->right))+1;
    }
}

int AVL::getFactor(Node* n){
    return getHeight(n->left) - getHeight(n->right);
}

void AVL::rotateLeft(Node*& n){
    Node* right = n->right;  // n不存在？或n->right不存在？
    n->right = right->left;
    right->left = n;
    n = right;
}

void AVL::rotateRight(Node*& n){
    Node* left = n->left;  // n不存在？或n->right不存在？
    n->left = left->right;
    left->right = n;
    n = left;
}

void AVL::rebalance(Node*& n){
    if(n == nullptr) return;
    int factor = getFactor(n);
    cout << "Node " << n->data << " factor " << factor << endl;
    // if(factor>1){
    //     cout << getFactor(n->left) << endl;
    // }
    if(factor>1 && getFactor(n->left)>=0){
        rotateRight(n);
    }else if(factor>1 && getFactor(n->left)<0){
        rotateLeft(n->left);
        rotateRight(n);
    }else if(factor<-1 && getFactor(n->right)<=0){
        rotateLeft(n);
    }else if(factor<-1 && getFactor(n->right)>0){
        rotateRight(n->right);
        rotateLeft(n);
    }
}

bool AVL::insertVal(int val){
    return insertValHelper(root, val);
}

bool AVL::insertValHelper(Node *&n, int val){
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
    rebalance(n);
    return true;
}

bool AVL::deleteVal(int val){
    return deleteValHelper(root, val);
}

bool AVL::deleteValHelper(Node *&n, int val){
    if(n == nullptr){return false;}
    if(val == n->data){
        deleteNode(n);
    }else if(val > n->data){
        deleteValHelper(n->right, val);
    }else{
        deleteValHelper(n->left, val);
    }
    rebalance(n);
    return true;
}

bool AVL::deleteNode(Node *&n){
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

void AVL::printTree(void){
    cout << "print" << endl;
    // inOrderTraversal(root);
    levelTraversal(root);
    cout << endl;
}

void AVL::inOrderTraversal(Node *n){
    if(n == nullptr) return;
    inOrderTraversal(n->left);
    cout << n->data << " ";
    inOrderTraversal(n->right);
}

void AVL::levelTraversal(Node* n){
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

bool AVL::searchNode(int val){
    return searchNodeHelper(root, val);
}

bool AVL::searchNodeHelper(Node *n, int val){
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
    AVL T;
    // int arr[] = {9, 12, 5, 3, 4, 1, 38};
    // T.insertVal(2);
    // T.insertVal(3);
    // T.insertVal(5);

    // int arr[] = {50,25,10,5,2,9};
    // for(auto i:arr){
    //     T.insertVal(i);
    // }
    // T.printTree();
    // T.deleteVal(5);
    // T.printTree();

    // int arr[] = {50, 25, 15, 10, 2, 1, -20, -30};
    // for(auto i:arr){
    //     T.insertVal(i);
    //     // T.printTree();
    // }
    // T.printTree();

    // for(int i=0;i<200;i++){
    //     T.insertVal(i);
    // }
    // T.printTree();

    // cout << "delete: " << endl;
    // for(int i=100;i<200;i++){
    //     T.deleteVal(i);
    // }
    // T.printTree();

    // for(int i=0;i<200;i++){
    //     T.insertVal(i);
    // }
    // T.printTree();

    // int arr[] = {50,25,10,5,2,9,18,17,16,15,14};
    int arr[] = {50,25,10,5,2,9};
    for(auto i:arr){
        T.insertVal(i);
    }
    T.printTree();
    T.deleteVal(50);
    T.printTree();
    T.deleteVal(25);
    T.printTree();

    // cout << "search" << T.searchNode(99) << endl;
    // cout << "search" << T.searchNode(2) << endl;
    // cout << "search" << T.searchNode(9) << endl;
    // cout << "search" << T.searchNode(-200) << endl;
    
    cout << "end" << endl;
}
