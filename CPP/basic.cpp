#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <unordered_map>
using namespace std;

class A{
public:
    inline static int a=10;
};

int foo(void){
    static int a = 3;
    a++;
    return a;
}

typedef struct Student{
    int num=0;
    string name;
    double score=0;
}Students;

pair<int, int> testf(){
    return make_pair(1, 2);
}

void lambda_value_capture() {
    int value = 1;
    auto copy_value = [value](int a) {
    return value*a;
    };
    value = 100;
    auto stored_value = copy_value(2);
    std::cout << "stored_value = " << stored_value << std::endl;
    // 这时, stored_value == 1, 而 value == 100.
    // 因为 copy_value 在创建时就保存了一份 value 的拷贝
}
    

int main(){
    // Students a={0, "amy", 100};
    // int c,d;
    // pair<int, int> e;
    // e = testf();
    unordered_map<int, int> a;
    a[3] = 2;
    a[2] += 1;
    for(auto [k,v]: a){
        cout << "k" << k << "v" << v << endl;
    }
    lambda_value_capture();
    return 0;
}

