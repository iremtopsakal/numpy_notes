#NUMPY in 1D

import numpy as np
a = np.array([0,1,2,3,4])
#type(a) : numpy.ndarray
#a.dtype : dtype('int64')
#a.size : 5
#a.ndim: 1 --> (dimension)
#a.shape: (5,) --> (a tuple of integers indicating the size of the array in each dimension.)

####Arrays are mutable
a[0]=100 #a: [100,1,2,3,4]
d=a[1:4] #d: [1,2,3]
a[3:5]=300,400 #a: [100,1,2,300,400]

####Arrays as vectors

        # u = [1,2]
        # v = [3,1]
        # z=[]
        # for n,m in zip(u,v):
        #     z.append(n+m)

u = np.array([1,2])
v = np.array([3,1])
z = u + v # z: array([4,3)]

w = 2*u # w: [2,4] -->  scalar multiplication
q = u*v # q: [3,2] --> x'ler kendi aralarında, y'ler kendi aralarında  çarpım
e = np.dot(u,v) # e: 5 --> dot product
r = u + 1 # r: [1+1,2+1] --> broadcasting

####Universal functions
s = np.array([1,-1,1,-1])
ms = s.mean() # s: 1/4(1-1+1-1) = 0 = s:0 -->  mean (average)
std = s.std() # standard deviation


b = np.array([1,-2,3,4,5])
mxb = b.max() # mxb: 5 --> maximum value
mnb = b.min()

np.pi # π number
x = np.array([0,np.pi/2,np.pi]) # x: [0,π/2,π]
y = np.sin(x) # y: [sin(0),sin(π/2),sin(π)] = [0,1,0]

np.linspace(-2,2, num=5) # [-2,-1,0,1,2]
np.linspace(-2,2, num=9) # [-2,-1.5,-1,-0.5,0,0.5,1,1.5,2]

l = np.linspace(0, 2*np.pi, 100) # 100 --> num=100
f = np.sin(l)

import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(l,f)

####Plotting settings
# def Plotvec1(u, z, v):
#
#     ax = plt.axes()
#     ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
#     plt.text(*(u + 0.1), 'u')
#
#     ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
#     plt.text(*(v + 0.1), 'v')
#     ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
#     plt.text(*(z + 0.1), 'z')
#     plt.ylim(-2, 2)
#     plt.xlim(-2, 2)
#
# def Plotvec2(a,b):
#     ax = plt.axes()
#     ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
#     plt.text(*(a + 0.1), 'a')
#     ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
#     plt.text(*(b + 0.1), 'b')
#     plt.ylim(-2, 2)
#     plt.xlim(-2, 2)
