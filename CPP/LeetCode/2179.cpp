#include<iostream>
#include<vector>
#include<cassert>
#include<unordered_map>
using namespace std;

class Solution {
    public:
        long long goodTriplets(vector<int>& nums1, vector<int>& nums2) {
            /*
            思路1 找到一种nlogn时间内求出一个nums内所有good triplet的方法
            先求一个 加入set 然后再求第二个 如果在set内就计数
            问题1 能找到一个算法在nlogn时间内枚举gt吗

            找到从0开始的最长递增序列 (0,b,e)
            找到从i开始的最长递增序列 (i,b,e)
            i-1开始的最长递增序列 (i-1, ) + 下一个比i-1大的值的最长递增序列

            现在的问题是 有了这样的序列要怎样使用呢 如果要遍历triplet似乎还是绕不过时间复杂度O(n^2)
            
            如果每一时刻，同时有nums1和nums2的(i,b,e)那么答案只可能是他们交集的排列
            进一步，如果从尾部迭代地开始：
            如果i1-1 <= i1且i2-1 <= i2，则计算并继续迭代
            如果i1-1 > i1且i2-1 <= i2，此时是否需要吸收i2？
            如果i1-1 <= i1且i2-1 > i2,
            如果i1-1 > i1且i2-1 > i2，直接同时跳过
            这样就存在一个问题，那些被跳过的值还可能在其他情况下构成gt吗？

            思路2 找到i之前比i小的所有值和i之后比i大的所有值
            对于每一个i有i_left * i_right个gt
            */

            // vector<int> t1={1,2,5,2,999,333};
            // cout << t1.back() << endl;
            cout << "****************** being ******************" << endl;
            vector<int> last_vector(nums1.size()), first_vector(nums1.size());
            for(int i=0;i<nums1.size();i++){
                last_vector[nums1[i]] = i;
                first_vector[nums1[i]] = i;
            }

            for(int i=0;i<nums2.size();i++){
                last_vector[nums2[i]] = max(last_vector[nums2[i]], i);
                first_vector[nums2[i]] = min(first_vector[nums2[i]], i);
            }

            vector<int> left_num(nums1.size()), right_num(nums1.size());
            for(int i=0;i<nums1.size();i++){
                left_num[last_vector[i]] += 1; 
                right_num[first_vector[i]] += 1; 
            }
            
            for(int i=1;i<left_num.size();i++){
                left_num[i] += left_num[i-1];
            }

            for(int i=left_num.size()-2;i>=0;i--){
                right_num[i] += right_num[i+1];
            }

            cout << "left_num" << endl;
            for(auto i:left_num){
                cout << i << " ";
            }
            cout << endl;

            cout << "right_num" << endl;
            for(auto i:right_num){
                cout << i << " ";
            }
            cout << endl;

            long long ret=0;

            for(int i=1;i<nums1.size()-1;i++){
                //同时找nums1前面的小值
                if(nums1[i]==nums2[i])
                    ret += left_num[i-1]*right_num[i+1];
            }
            cout << "ret " << ret << endl;
            cout << "****************** end ******************" << endl;
            return ret;
        }
    };

int main(void){
    Solution s;
    vector<int> nums1, nums2;
    long long res, ans;
    // case bug
    // nums1 = {13,14,10,2,12,3,9,11,15,8,4,7,0,6,5,1};
    // nums2 = {8,7,9,5,6,14,15,10,2,11,4,13,3,12,1,0};
    // res = s.goodTriplets(nums1, nums2);
    // ans = 77;
    // assert(res == ans);
    // case std1
    nums1 = {2,0,1,3};
    nums2 = {0,1,2,3};
    res = s.goodTriplets(nums1, nums2);
    ans = 1;
    assert(res == ans);
    // case std2
    nums1 = {4,0,1,3,2};
    nums2 = {4,1,0,2,3};
    res = s.goodTriplets(nums1, nums2);
    ans = 4;
    assert(res == ans);
}