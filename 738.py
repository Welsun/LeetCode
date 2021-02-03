

class Solution:
    """
    给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

    （当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
    """
    def monotoneIncreasingDigits(self, N: int) -> int:

        if (N // 10) == 0:
            return N
        nums=[]
        while N // 10 > 0:
            nums.append(N % 10)
            N = N // 10
        nums.append(N)
        nums = nums[::-1]
        print(nums)
        return self.get(nums)



    def get(self,nums):
        if len(nums)==1:
            return nums
        



    def judge(self,N):
        nums = []
        while N // 10 > 0:
            nums.append(N % 10)
            N = N // 10
        nums.append(N)
        nums = nums[::-1]
        print(nums)
        flag = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                flag = False
        return flag






if __name__ == '__main__':
    import time
    time1=time.time()
    sol=Solution()

    N=393457075
    print(sol.monotoneIncreasingDigits(N=N))
    print(time.time()-time1)