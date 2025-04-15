from typing import List
from line_profiler import profile
from functools import lru_cache

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        # [3, 25, 50, 100, 200]
        # [3, 25, 40, 100, 200]
        ret = []
        for i in range(len(nums)):
            tmp_list = [nums[i]]
            for j in range(i+1, len(nums)):
                if nums[j]%tmp_list[-1] == 0:
                    tmp_list.append(nums[j])
            if len(tmp_list) > len(ret):
                ret = tmp_list
            print(tmp_list)
        print(ret)
        return ret

    @profile
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        # [3, 25, 50, 100, 200]
        # [3, 25, 40, 100, 200]
        ret = []
        def dfs(find, idx):
            nonlocal ret
            if idx >= len(nums):
                # update find
                if len(find) > len(ret):
                    ret = find.copy()
                return

            if nums[idx]%find[-1] == 0:
                find.append(nums[idx])
                dfs(find, idx+1)
                find.pop()
            dfs(find, idx+1)
            return
        
        for i in range(len(nums)):
            dfs([nums[i]], i+1)
        print(ret)
        return ret

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        # [3, 25, 50, 100, 200]
        # [3, 25, 40, 100, 200]
        ret = []
        def dfs(find, idx):
            nonlocal ret
            if idx >= len(nums):
                # update find
                if len(find) > len(ret):
                    ret = find.copy()
                return

            while idx<len(nums) and nums[idx]%find[-1] != 0:
                idx += 1
            if idx == len(nums):
                dfs(find, idx+1)
                return
            find.append(nums[idx])
            dfs(find, idx+1)
            find.pop()
            dfs(find, idx+1)

            return
        
        for i in range(len(nums)):
            dfs([nums[i]], i+1)
        print(ret)
        return ret

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        ret = []
        @lru_cache(None)
        def dfs(idx):
            if idx >= len(nums):
                return []
            
            j = idx+1
            while j<len(nums) and nums[j]%nums[idx] != 0:
                j += 1
            if idx == len(nums):
                return []
            
            l1 = dfs(j)
            l2 = dfs(j+1)
            return [nums[idx]] + (l1 if len(l1)>len(l2) else l2)

        for i in range(len(nums)):
            tmp = dfs(i)
            if len(tmp) > len(ret):
                ret = tmp
        print("ret", ret)
        return ret

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        ret = []
        @lru_cache(None)
        def dfs(idx):
            if idx >= len(nums):
                return []
            
            optimal = []
            for i in range(idx+1, len(nums)):
                if nums[i] % nums[idx] == 0:
                    l = dfs(i)
                    if len(l) > len(optimal):
                        optimal = l
            return [nums[idx]] + optimal
        
        for i in range(len(nums)):
            tmp = dfs(i)
            if len(tmp) > len(ret):
                ret = tmp
        print("ret", ret)
        return ret

su = Solution()


# case tle
nums = [480,812,614,116,368,538,570,423,883,441,81,262,18,696,985,911,627,479,114,455,539,290,733,536,469,349,621,432,898,595,794,378,407,845,774,944,414,548,178,854,981,439,872,676,775,782,303,605,247,109,143,888,193,31,357,542,3,140,791,598,933,520,356,691,365,129,634,778,29,163,984,9,953,855,684,80,988,338,587,799,827,474,991,857,182,884,859,322,675,808,606,546,297,910,644,282,40,672,797,23,680,749,877,715,828,216,405,864,802,555,690,276,545,809,781,108,482,807,916,88,352,430,736,73,17,301,96,165,323,127,914,551,842,93,766,308,920,152,997,547,48,246,355,354,837,986,50,11,475,379,899,544,221,697,123,890,253,240,487,561,159,638,557,705,37,155,412,865,860,600,850,875,835,881,885,433,263,331,277,806,903,973,966,377,862,219,617,348,779,337,687,832,725,841,243,589,700,531,68,625,764,952,58,470,566,740,746,724,995,70,689,371,931,907,987,630,685,318,372,945,43,564,983,616,732,421,498,398,261,102,731,19,742,540,431,180,249,810,374,714,97,10,521,12,900,856,631,125,25,737,234,831,467,647,346,268,128,530,723,817,131,844,363,990,235,1,753,90,980,718,104,868,840,573,659,706,949,305,51,568,200,98,274,347,228,510,224,229,458,381,208,468,663,335,358,503,788,513,493,582,169,896,150,599,993,124,826,248,77,591,876,535,171,608,434,75,402,393,409,111,895,549,759,41,326,927,288,646,417,250,254,921,196,367,332,592,406,489,166,103,847,494,107,173,773,999,418,424,408,54,604,874,682,869,281,273,317,38,265,204,719,893,917,738,375,121,280,635,863,39,688,642,761,517,359,198,822,387,438,232,157,436,500,74,227,35,699,602,314,333,465,20,994,112,285,813,233,275,526,853,560,873,576,255,534,783,188,194,824,199,823,800,330,117,225,553,628,777,300,803,729,105,703,562,982,905,671,609,340,942,22,902,351,816,934,662,712,287,46,241,504,861,78,463,744,192,257,271,190,86,339,66,935,176,291,373,975,752,187,658,266,1000,879,979,704,507,21,790,461,207,906,341,717,796,623,295,556,821,134,130,833,336,962,220,968,956,264,416,886,710,577,364,755,620,312,648,329,87,284,442,362,681,661,147,383,829,567,444,528,818,711,388,218,814,529,747,735,460,395,789,84,750,913,316,891,767,120,655,307,294,543,728,518,950,99,195,665,245,978,762,34,471,191,279,223,376,113,922,709,758,701,580,686,490,596,588,446,901,386,15,419,894,205,33,299,306,457,56,175,82,996,532,497,552,870,618,36,678,426,92,151,533,792,126,527,811,707,144,967,310,492,158,133,563,963,145,653,670,488,632,525,726,915,572,919,483,514,930,231,908,396,16,28,892,64,501,610,369,722,804,242,836,846,76,702,909,49,213,14,516,382,466,286]
res = su.largestDivisibleSubset(nums)
ans = [9,18,90,180,360,720]
# assert(res == ans)



# case bug1
nums = [5,9,18,54,108,540,90,180,360,720]
res = su.largestDivisibleSubset(nums)
ans = [9,18,90,180,360,720]
assert(res == ans)



# case std1
nums = [1,2,3]
res = su.largestDivisibleSubset(nums)
ans = [1,2]
assert(res == ans)

# case std1
nums = [1,2,4,8]
res = su.largestDivisibleSubset(nums)
ans = [1,2,4,8]
assert(res == ans)
