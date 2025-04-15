#include<iostream>
#include<vector>
#include<cassert>
#include<set>
#include<algorithm>
#include<unordered_map>
#include<string>
#include<sstream>

using namespace std;

class Solution {
    public:
        int minOperations(vector<int>& nums) {
            // 暴力方法：从每个位置开始，翻转三个。停止条件怎么处理？
            // 从上面的问题引申：能否直接判断一个nums是否有解？
            // 猜想：
            // 能化为全0的nums和化为全1的nums之间有关系吗？
            // 总nums长度和初始0、1个数对解的存在性有何影响？
            // 是否存在最优子结构？如[000010101]开头有连续三个0时，直接化简子问题？
            // 每一步都有n-2种选择，复杂度(n-2)^x
            // 暴力法甚至面临无法收敛的问题？如何确定当前状态是更好而不是更差？
            // 累加数组？
            // 只要当前有0就反转：(1)这样做一定是最优解吗？（2）这样做会排除有效解吗？
            /*最优的证明：
                0xxxxxxx的序列(0110)：
                假设存在解，如果取前三位翻转，则后续1(yyxxxxx)中(yyxxxxx)也需要是最优
            */
            // nums_cnt: [1,1,1]
            // [0,1,1,1,0,0]
            /*
            [0,1,1,1,0,0] 第一步，有四种选择(011) 111 110 100
            [1,0,0,1,0,0] 第二步，有四种选择 100  001 010 100
            一种观点：将两个步骤合为一步来看， xxxxxx
            */
            /*
            为什么无解？
            [0,1,1,1] [0,0,0,0] [1,1,1,0] [1,0,0,1]
            从一个全1nums开始，可以衍生出多少种nums？
            111->000
            1111->0001->0110->1000->1111

            invlaid: 0011 0010 0100 0101
            invlaid: 1101 1010 1011 1100
            invlaid: 0111 0000 1110 1001
              valid: 1111 0001 0110 1000
            对称性、余3

            全0和全1如果能连通，意味着什么？
            */
           int i=0, cnt=0;
           while(i<nums.size()-2){
                if(nums[i]==0){
                    nums[i] ^= 1;
                    nums[i+1] ^= 1;
                    nums[i+2] ^= 1;
                    cnt++;
                }
                i++;
           }
           return (nums[nums.size()-1]==0|nums[nums.size()-2]==0)?-1:cnt;
        }
    };

int main(void){
    Solution s;
    vector<int> nums;
    int res, ans;
    // case std1
    nums = {0,1,1,1,0,0};
    res = s.minOperations(nums);
    cout << "res: " << res << endl;
    ans = 3;
    // case std2
    nums = {0,1,1,1};
    res = s.minOperations(nums);
    cout << "res: " << res << endl;
    ans = -1;
    assert(res == ans);
    // case1
    nums = {0,0,0,1};
    res = s.minOperations(nums);
    cout << "res: " << res << endl;
    ans = 1;
    // case2
    nums = {0,1,1,0};
    res = s.minOperations(nums);
    cout << "res: " << res << endl;
    ans = 2;
    assert(res == ans);
    // case3
    nums = {1,0,0,0};
    res = s.minOperations(nums);
    cout << "res: " << res << endl;
    ans = 1;
    assert(res == ans);
    // case1 optimal 第一位没有翻转，但实际上翻转后更优
    nums = {1,0,1,0,0};
    res = s.minOperations(nums);
    cout << "res: " << res << endl;
    ans = -1;
    assert(res == ans);
}
