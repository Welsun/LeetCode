import bisect

class Solution:
    """
    给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。
    窗口中有 k 个数，每次窗口向右移动 1 位。
    你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。
    """

    def medianSlidingWindow1(self, nums, k):
        """速度慢5396ms,内存16MB"""
        result=[]
        for i in range(len(nums)-k+1):
            window=nums[i:i+k]

            median=self.get_median(sorted(window))
            result.append(median)
        return result

    def medianSlidingWindow2(self, nums, k):
        """结合二分查找,316ms"""
        l=len(nums)
        a=sorted(nums[:k])
        result=[self.get_median(a)]
        for i in range(l-k):
            #print(a)
            j=i+k
            a.remove(nums[i])
            a.insert(bisect.bisect_left(a,nums[j]),nums[j])
            result.append(self.get_median(a))

        return result


    def get_median(self,window):
        if len(window) %2 ==0:
            return (window[len(window)//2-1]+window[len(window)//2])/2
        else:
            return window[len(window)//2]


if __name__ == '__main__':
    nums=[1,3,-1,-3,5,3,6,7]
    s=Solution()
    print(s.medianSlidingWindow2(nums,k=3))

