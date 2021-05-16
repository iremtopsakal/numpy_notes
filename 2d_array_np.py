#NUMPY in 2D

import numpy as np

a=[[11,12,13],[21,22,23],[31,32,33]]
A=np.array(a) #    [ 11 12 13 ]
              # A: | 21 22 23 |
              #    [ 31 32 33 ]
#A.ndim: 2 --> 2D Array
#A.shape: (3,3) --> (row, collums)
#A.size: 9

#    [ 11 12 13 ]     [ A[0][0]  A[0][1]  A[0][2] ]       [ A[0,0]  A[0,1]  A[0,2] ]
# A: | 21 22 23 | =>  [ A[1][0]  A[1][1]  A[1][2] ] =>    [ A[1,0]  A[1,1]  A[1,2] ]
#    [ 31 32 33 ]     [ A[2][0]  A[2][1]  A[2][2] ]       [ A[2,0] A[2,1]  A[2,2] ]

A[0, 0:2] # slicing --> [11,12]
A[0:2, 2] # --> [13,23]

X = np.array([[1,0],[0,1]])
Y = np.array([[2,1],[1,2]])
Z = X + Y # Z: array([[3,1],[1,3]]) --> matrix addition
Q = 2*Y # Q: array([[4,2],[2,4]])  --> scalar multiplication
W = X*Y # X: array([[1*2,0*1],[0*1,1*2]]) = array([[2,0],[0,2]]) --> Hadamard product

B = np.array([[0,1,1],[1,0,1]])
C = np.array([[1,1],[1,1],[-1,1]])
D = np.dot(B,C) #C: array([[0,2],[0,2]]) --> matrix multiplication

D.T # transpose of D
