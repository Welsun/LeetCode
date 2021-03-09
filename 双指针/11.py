# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。


class Solution:
    def maxArea(self, height):
        ##双指针法，击败 5%
        left=0
        right=len(height)-1
        maxv=0
        while left!=right:
            temp= (right-left) * min(height[left],height[right])
            maxv=max(temp,maxv)
            if height[left]< height[right]:
                left+=1
            else:
                right-=1

        return maxv
    # def maxArea(self, height):
    #     """
    #     自想，分治法
    #     超时
    #     :param height:
    #     :return:
    #     """
    #     if len(height)<2:
    #         return 0;
    #     if len(height)==2:
    #         return min(height)
    #     mid=len(height)//2
    #     left=height[:mid]
    #     right=height[mid:]
    #     left_max=self.maxArea(left)
    #     right_max=self.maxArea(right)
    #
    #     middel_max=0
    #     for i in range(len(left)):
    #         for j in range(len(right)):
    #             temp=(j+len(left)-i)*min(left[i],right[j])
    #             if temp > middel_max:
    #                 middel_max=temp
    #     return max([left_max,right_max,middel_max])

if __name__ == '__main__':
    S=Solution()
    height=[1,8,6,2,5,4,8,3,7]
    print(S.maxArea(height))