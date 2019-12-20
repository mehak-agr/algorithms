class Solution:
    def dfs(A: List[List[int]], B: List[List[int]], i, j):
        B[i][j]=1
        if (i+1)<len(A) and A[i+1][j]==1 and B[i+1][j]==0:
            Solution.dfs(A,B,i+1,j)
        if (i)>0 and A[i-1][j]==1 and B[i-1][j]==0:
            Solution.dfs(A,B,i-1,j)
        if (j+1)<len(A[0]) and A[i][j+1]==1 and B[i][j+1]==0:
            Solution.dfs(A,B,i,j+1)
        if (j)>0 and A[i][j-1]==1 and B[i][j-1]==0:
            Solution.dfs(A,B,i,j-1)
        return
    def sum(A) -> int:
        s=0
        for i in range(len(A)):
            for j in range(len(A[0])):
                s=s+A[i][j]
        return s
    def numEnclaves(self, A: List[List[int]]) -> int:
        r=len(A)
        c=len(A[0])
        B=[[0 for col in range(c)] for row in range(r)]
        for j in range(c):
            if B[0][j]==0 and A[0][j]==1:
                print('1- ','r:',0,' c:',j)
                Solution.dfs(A,B,0,j)
        for j in range(c):
            if B[r-1][j]==0 and A[r-1][j]==1:
                print('2- ','r:',r-1,' c:',j)
                Solution.dfs(A,B,r-1,j)
        for i in range(r):
            if B[i][0]==0 and A[i][0]==1:
                print('3- ','r:',i,' c:',0)
                Solution.dfs(A,B,i,0)
        for i in range(r):
            if B[i][c-1]==0 and A[i][c-1]==1:
                print('4- ','r:',i,' c:',r-1)
                Solution.dfs(A,B,i,c-1)
        C=[[0 for col in range(c)] for row in range(r)]
        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j]=A[i][j]-B[i][j]
        print(C)
        return Solution.sum(A)-Solution.sum(B)
