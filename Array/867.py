class Solution:
    """
    给定一个矩阵 A， 返回 A 的转置矩阵。
    """
    def transpose(self, A):
        m=len(A)
        n=len(A[0])
        result=[]

        for i in range(n):
            row = []
            for j in range(m):
                row.append(A[j][i])
            result.append(row)

        return result



if __name__ == '__main__':

    s=Solution()
    print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))
