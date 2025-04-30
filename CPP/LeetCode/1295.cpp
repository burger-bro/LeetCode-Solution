class Solution {
    public:
        int findNumbers(vector<int>& nums) {
            int ret=0, digitCnt=0;
            for(auto n: nums){
                digitCnt=0;
                while(n){
                    n/=10;
                    digitCnt++;
                }
                if(digitCnt%2==0){
                    ret++;
                }
            }
            return ret;
        }
    };