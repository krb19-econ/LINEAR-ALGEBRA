import sys
print(sys.version)

import numpy as np
import scipy.linalg as la

#FIRST IN DETAIL

A = np.array([[1,0,4],[5,3,9],[1,2,3]])
print(A)

B = np.array([[4,1,3],[1,2,2],[3,4,5]])
print(B)

one = np.array(la.solve(B, A.T[0]))

two = np.array(la.solve(B, A.T[1]))

three = np.array(la.solve(B, A.T[2]))

#Required transformation matrix
tran = np.column_stack((one,two,three))
tran

Now to create a function for the same

#Now creating a function
def transformation(old_basis, new_basis):
    tran = np.random.random((np.shape(A)[0],1))
    for i in list(range(A.shape[1])):
        tran = np.c_[tran, np.array(la.solve(B, A.T[i]))]
    return tran[:,1:]

transformation(A,B)
