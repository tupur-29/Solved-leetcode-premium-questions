class Solution:
    def celebrity(self, mat):
        # code here
        top=0
        down=len(mat)-1
        while top<down:
            if mat[top][down]==1:
                top+=1
            else:
                down-=1
            
        if top>down:
            return -1
        for i in range(len(mat)):
            if i==top:
                continue
            if mat[top][i]==1 or mat[i][top]==0:
                return -1
        return top
