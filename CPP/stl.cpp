#include <iostream>
#include <vector>
using namespace std;

void vector_test(){
    vector<int> v1;
    cout << "size = " << v1.size() << endl;
    for(int i=0;i<5;i++){
        v1.push_back(i);
    }
    cout << "size = " << v1.size() << endl;
    vector<int>::iterator it = v1.begin();
    while(it != v1.end()){
        cout << "v = " << *it++ << endl;
    }
    for(auto it:v1){
        cout << "v2 = " << it << endl;
    }
}

int main(){
    vector_test();
}
