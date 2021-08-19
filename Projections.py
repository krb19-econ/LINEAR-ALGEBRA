import sys
print(sys.version)

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
%matplotlib inline

#VECTOR PROJECTION

def vec_proj(v,u):
    """
    Provides projection of vector v on u
    """
    p = ((u@v)/la.norm(u)**2)*u
    return p

v = np.array([2,3])
u = np.array([1,0])
vec_proj(v,u)



#ORTHOGONAL PROJECTION INTO SUBSPACE

def sub_proj_mat(A):
    """
    Function to form projection matrix 
    """
    P = A@la.inv((A.T)@A)@A.T
    return P

A = np.array([[1,2],[3,4]])
sub_proj_mat(A)

