import sys
print(sys.version)

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

The function scipy.linalg.eig computes eigenvalues and eigenvectors of a square matrix. It returns the values in the form of a tuple and can be unpacked 

#Let 
A = np.array([[1,5],[2,4]])
print(A)

la.eig(A)

#The first two values are the eigenvalues of the matrix.  
#The next matrix contains the eigenvectors 
#Unpacking as a tuple

eigenval, eigenvec = la.eig(A)

print(eigenval)

print(eigenvec)

B = np.array([[9,-1],[5,7]])
print(B)

la.eig(B)

In above case we get complex eig which always come in pairs,  
Symetric matrices however always have real eigenvalues and their vectors are orthogonal

C = np.array([[1,2,3],[2,9,5],[3,5,6]])
print(C)

evals,evecs = la.eig(C)
evals

#To get real values
evals = evals.real
evals

evecs

#Multiplying the first 2 columns
evecs[:,0]@evecs[:,1]

a = np.array([1,2,3])
b = np.array([[4],[5],[6]])
a@b



#DIAGONALIZATION

#M is diagonalizable if there exists an invertible matrix $P$ such that $D = P^{-1}MP$ is a diagonal matrix.  
#A further result in linear algebra is that a square matrix $M$ of size $n$ is diagonalizable if and only if $M$ has $n$ independent eigevectors. Furthermore, $M = PDP^{-1}$ where the columns of $P$ are the eigenvectors of $M$ and $D$ has corresponding eigenvalues along the diagonal.

#Example 1 we take eigenvalues and eigenvectors as given

D = np.diag((3,1))
print(D)

P = np.array([[1,1],[1,-1]])
print(P)

#Hence;
M = P@D@la.inv(P)
print(M)

#To confirm
la.eig(M)

#NOTE: The formula returns nonrmalized eigenvectors. Mentioned in the info

