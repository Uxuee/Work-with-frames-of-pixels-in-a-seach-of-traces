# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 21:48:18 2019

@author: Ariadna
"""

import os
from conteo import Conteo
from Compare import Compare
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



i=0
a=3

path = 'D:\data_y_200gama0z'

files = {}


# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.npy' in file:
            files[i]=os.path.join(r, file)
            i+=1

sum={}


for u in range(i):
    if not u==a:
        X=[]
        Y=[]
        U=Compare(files[u],files[u+1])
        a=u+1
        num=Conteo(U)
        for key in num: 
            if key in sum: 
                sum[key] = sum[key] + num[key] 
            else: 
                sum[key] = num[key]
                

for key in sorted(sum.keys()):
    X.append(key)
    Y.append(sum[key])
            
plt.plot(X,Y)
plt.xlim(-60, 60)
#plt.xticks(np.arange(-50, 50, step=5))

plt.yscale('log')
#        plt.xscale('log')
        
plt.savefig('todo.png')

plt.clf() 
