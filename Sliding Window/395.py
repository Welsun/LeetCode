# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串，
# 要求该子串中的每一字符出现次数都不少于 k 。
# 返回这一子串的长度
from collections import Counter

class Solution:
    def longestSubstring(self, s, k):
        n=len(s)
        max_len=0

        for t in range(1,27):
            left = 0
            right = 0
            less=0
            total=0
            cnt = [0] * 26
            while right<n:
                idx=ord(s[right])-ord("a")
                cnt[idx]+=1
                if cnt[idx]==1:
                    total+=1
                    less+=1
                if cnt[idx]==k:
                    less-=1

                while total > t:
                    idx=ord(s[left])-ord("a")
                    cnt[idx]-=1

                    if cnt[idx]==0:
                        total-=1
                        less-=1
                    if cnt[idx]==k-1:
                        less+=1
                    left+=1
                if less==0:
                    max_len=max(max_len,right-left+1)
                right+=1





        return max_len


if __name__ == '__main__':
    S=Solution()
    s="ababbc"

    k=2
    #print([0]*26)
    print(S.longestSubstring(s,k))